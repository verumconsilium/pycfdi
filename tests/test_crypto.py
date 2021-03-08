import pycfdi.crypto
import unittest
import pathlib
import re
import os
from cryptography import x509
from cryptography.hazmat.primitives.asymmetric import rsa
from pycfdi import exceptions

TEST_PRIVATE_KEYS_PASSWORD = '12345678a'


class TestCrypto(unittest.TestCase):

    def test_leer_certificado_persona_moral(self):
        cer = self._get_certificado_prueba('persona_moral')

        self.assertIsInstance(cer, x509.Certificate)

    def test_leer_certificado_persona_fisica(self):
        cer = self._get_certificado_prueba('persona_fisica')

        self.assertIsInstance(cer, x509.Certificate)

    def test_convertir_certificado_a_base64(self):
        cer = self._get_certificado_prueba('persona_moral')
        cer_base64 = pycfdi.crypto.certificado_base64(cer)

        base64_regex = re.compile('^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$')
        self.assertTrue(base64_regex.match(cer_base64))

    def test_obtener_numero_certificado(self):
        cer_persona_moral = self._get_certificado_prueba('persona_moral')
        cer_persona_fisica = self._get_certificado_prueba('persona_fisica')

        self.assertEqual('30001000000400002429', pycfdi.crypto.no_certificado(cer_persona_moral))
        self.assertEqual('30001000000400002308', pycfdi.crypto.no_certificado(cer_persona_fisica))

    def test_leer_llave_privada(self):
        key = self._get_llave_privada_prueba('persona_moral')

        self.assertIsInstance(key, rsa.RSAPrivateKey)

    def test_error_al_utilizar_contrasena_incorrecta(self):
        path_str = os.path.join(os.path.dirname(__file__), 'certificados_prueba', 'persona_moral', 'llave_privada.key')
        path = pathlib.Path(path_str)
        key_bytes = path.read_bytes()

        with self.assertRaises(exceptions.crypto.IncorrectPasswordError):
            pycfdi.crypto.leer_llave_privada(key_bytes, 'Incorrecto')

    def test_sellar_bytes(self):
        key = self._get_llave_privada_prueba('persona_fisica')
        message = b'foobar'

        signed = pycfdi.crypto.sellar(message, key)

        self.assertValidSignature(key.public_key(), signed, message)

    def test_sellar_str(self):
        key = self._get_llave_privada_prueba('persona_fisica')
        message = 'foobar'

        signed = pycfdi.crypto.sellar(message, key)

        self.assertValidSignature(key.public_key(), signed, message.encode())

    def assertValidSignature(self, public_key: rsa.RSAPublicKey, signedBase64: str, message: bytes):
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.asymmetric import padding
        import base64

        # si la firma es invalida, este metodo arroja una excepcion
        public_key.verify(
            base64.b64decode(signedBase64),
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        self.assertTrue(True)


    @staticmethod
    def _get_certificado_prueba(tipo_persona: str) -> x509.Certificate:
        path_str = os.path.join(os.path.dirname(__file__), 'certificados_prueba', tipo_persona, 'certificado.cer')
        path = pathlib.Path(path_str)

        cer_bytes = path.read_bytes()
        return pycfdi.crypto.leer_certificado(cer_bytes)

    @staticmethod
    def _get_llave_privada_prueba(tipo_persona: str) -> rsa.RSAPrivateKey:
        path_str = os.path.join(os.path.dirname(__file__), 'certificados_prueba', tipo_persona, 'llave_privada.key')
        path = pathlib.Path(path_str)
        key_bytes = path.read_bytes()

        return pycfdi.crypto.leer_llave_privada(key_bytes, TEST_PRIVATE_KEYS_PASSWORD)

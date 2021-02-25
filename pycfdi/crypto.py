import base64
import hashlib
from typing import Union
from cryptography.x509 import Certificate, load_der_x509_certificate
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey
from cryptography.hazmat.primitives.serialization import Encoding, load_der_private_key
from cryptography.hazmat.primitives.asymmetric import padding


def leer_certificado(cer_bytes: bytes) -> Certificate:
    return load_der_x509_certificate(cer_bytes)


def leer_llave_privada(key_bytes: bytes, password: str) -> RSAPrivateKey:
    return load_der_private_key(key_bytes, password=password.encode())


def sellar(message: Union[bytes, str], private_key: RSAPrivateKey) -> str:
    if isinstance(message, str):
        message = message.encode()

    prehashed_bytes = hashlib.sha256(message).hexdigest().encode()

    signed = private_key.sign(
        prehashed_bytes,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    return base64.b64encode(signed).decode('ascii')


def certificado_base64(cer: Certificate) -> str:
    encoding = Encoding('DER')
    cer_bytes = cer.public_bytes(encoding)
    base64_bytes = base64.b64encode(cer_bytes)

    return base64_bytes.decode('ascii')


def no_certificado(cer: Certificate) -> str:
    hex_serial_number = '%x' % cer.serial_number
    serial = ''

    for i in range(len(hex_serial_number)):
        if i % 2 != 0:
            serial += hex_serial_number[i]

    return serial

import base64
from typing import Union
from pycfdi import exceptions
from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization


def leer_certificado(cer_bytes: bytes) -> x509.Certificate:
    return x509.load_der_x509_certificate(cer_bytes)


def leer_llave_privada(key_bytes: bytes, password: str) -> rsa.RSAPrivateKey:
    try:
        return serialization.load_der_private_key(key_bytes, password=password.encode())
    except ValueError as e:
        if 'Incorrect password' in str(e):
            raise exceptions.crypto.IncorrectPasswordError()
        raise e


def sellar(message: Union[bytes, str], private_key: rsa.RSAPrivateKey) -> str:
    if isinstance(message, str):
        message = message.encode()


    signed = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    return base64.b64encode(signed).decode('utf-8')


def certificado_base64(cer: x509.Certificate) -> str:
    encoding = serialization.Encoding('DER')
    cer_bytes = cer.public_bytes(encoding)
    base64_bytes = base64.b64encode(cer_bytes)

    return base64_bytes.decode('utf-8')


def no_certificado(cer: x509.Certificate) -> str:
    hex_serial_number = '%x' % cer.serial_number
    serial = ''

    for i in range(len(hex_serial_number)):
        if i % 2 != 0:
            serial += hex_serial_number[i]

    return serial

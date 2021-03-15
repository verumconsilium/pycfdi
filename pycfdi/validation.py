import re

RFC_GENERICOS = ['XAXX010101000', 'XEXX010101000']
RFC_PATTERN = r'^([A-ZÑ&]{3,4}) ?(?:- ?)?(\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])) ?(?:- ?)?([A-Z\d]{2})([A\d])$'


def is_valid_rfc(rfc: str, aceptar_generico: bool = False) -> bool:
    """
    Valida RFC contra patrón general
    y su digito verificador
    :param rfc:
    :param aceptar_generico: Considerar RFC Genérico como válido
    :return:
    """
    regex = re.compile(RFC_PATTERN)

    if not regex.match(rfc):
        return False

    digito_verificador = rfc[-1]
    rfc_sin_digito = rfc[0:-1]
    rfc_length = len(rfc_sin_digito)

    diccionario = "0123456789ABCDEFGHIJKLMN&OPQRSTUVWXYZ Ñ"
    indice = rfc_length + 1

    suma = 0
    # Ajuste para persona moral
    if rfc_length != 12:
        suma = 481

    for i in range(rfc_length):
        suma += diccionario.index(rfc_sin_digito[i]) * (indice - i)

    digito_esperado = 11 - suma % 11
    digito_esperado = '0' if digito_esperado == 11 else digito_esperado
    digito_esperado = 'A' if digito_esperado == 10 else digito_esperado

    return digito_verificador == str(digito_esperado) or \
        (aceptar_generico and rfc in RFC_GENERICOS)

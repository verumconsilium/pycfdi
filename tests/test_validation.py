import unittest
import pycfdi
from tests import DATOS_PERSONA_FISICA, DATOS_PERSONA_MORAL


class TestValidation(unittest.TestCase):
    def test_true_is_valid_rfc_for_valid(self):
        rfc = DATOS_PERSONA_MORAL['rfc']

        self.assertTrue(pycfdi.validation.is_valid_rfc(rfc))

    def test_true_for_valid_rfc_persona_fisica(self):
        rfc = DATOS_PERSONA_FISICA['rfc']

        self.assertTrue(pycfdi.validation.is_valid_rfc(rfc))

    def test_false_for_invalid_rfc_pattern(self):
        invalid_rfc_pattern = 'Invalid RFC'

        self.assertFalse(pycfdi.validation.is_valid_rfc(invalid_rfc_pattern))

    def test_false_for_valid_pattern_invalid__digito_verificador(self):
        rfc = DATOS_PERSONA_MORAL['rfc']
        # Cambiar digito verificador
        rfc = rfc[0:-1] + str(int(rfc[-1]) + 1)

        self.assertFalse(pycfdi.validation.is_valid_rfc(rfc))

    def test_false_for_rfc_generico(self):
        rfc_generico = 'XAXX010101000'

        self.assertFalse(pycfdi.validation.is_valid_rfc(rfc_generico))

    def test_true_for_rfc_generico_with_aceptar_rfc_generico(self):
        rfc_publico_general = 'XAXX010101000'
        rfc_publico_extranjero = 'XEXX010101000'

        is_valid_publico_general = pycfdi.validation.is_valid_rfc(rfc_publico_general, aceptar_generico=True)
        is_valid_publico_extranjero = pycfdi.validation.is_valid_rfc(rfc_publico_extranjero, aceptar_generico=True)

        self.assertTrue(is_valid_publico_general)
        self.assertTrue(is_valid_publico_extranjero)

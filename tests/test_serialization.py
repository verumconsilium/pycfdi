import unittest
from pycfdi import cfdv33, serialization
import xmlunittest


class TestSerialization(xmlunittest.XmlTestCase):
    def test_serialize_deserialize(self):
        comprobante_original = cfdv33.Comprobante(
            emisor=cfdv33.Comprobante.Emisor(nombre='Juan Perez', rfc='JPAN2839003F02'),
            receptor=cfdv33.Comprobante.Receptor(nombre='Pedro Sanchez')
        )

        xml = serialization.serialize(comprobante_original)

        self.assertXmlDocument(xml.encode())

        comprobante_deserializado = serialization.deserialize(xml, cfdv33.Comprobante)

        self.assertIsInstance(comprobante_deserializado, cfdv33.Comprobante)
        self.assertEqual(comprobante_original.__dict__, comprobante_deserializado.__dict__)

    def test_generar_cadena_original_desde_object(self):
        comprobante = cfdv33.Comprobante()
        cadena_original = serialization.cadena_original(comprobante)

        self.assertIsNotNone(cadena_original)



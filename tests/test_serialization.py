from pycfdi import cfdv33, serialization
import xmlunittest
import os


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

    def test_raises_error_when_no_xslt_could_be_found(self):
        xml = serialization.serialize(cfdv33.Comprobante())
        exception_msg = 'XSLT was not provided nor could it be found automatically for the object.'

        with self.assertRaises(ValueError) as ctx:
            serialization.cadena_original(xml)
            self.assertEqual(str(ctx.exception), exception_msg)

    def test_deserialize_from_path_str(self):
        path_str = os.path.join(os.path.dirname(__file__), 'xml_prueba', 'CFDI.xml')
        comprobante = serialization.deserialize(path_str)

        self.assertIsInstance(comprobante, cfdv33.Comprobante)

    def test_deserialize_from_path_object(self):
        path_str = os.path.join(os.path.dirname(__file__), 'xml_prueba', 'CFDI.xml')
        from pathlib import Path
        path = Path(path_str)
        comprobante = serialization.deserialize(path)

        self.assertIsInstance(comprobante, cfdv33.Comprobante)

    def test_deserialize_from_bytes(self):
        path_str = os.path.join(os.path.dirname(__file__), 'xml_prueba', 'CFDI.xml')
        from pathlib import Path
        path = Path(path_str)
        comprobante = serialization.deserialize(path.read_bytes())

        self.assertIsInstance(comprobante, cfdv33.Comprobante)

    def test_generates_cadena_original_from_xslt_url(self):
        xslt_url = 'http://www.sat.gob.mx/sitio_internet/cfd/3/cadenaoriginal_3_3/cadenaoriginal_3_3.xslt'

        cadena_original = serialization.cadena_original(cfdv33.Comprobante(), xslt_url)

        self.assertIsNotNone(cadena_original)

    def test_unmarshalls_complementos_into_types(self):
        from pathlib import Path
        from pycfdi.complementos import pagos10, timbre_fiscal_digitalv11

        path_str = os.path.join(os.path.dirname(__file__), 'xml_prueba', 'pago.xml')
        path = Path(path_str)
        comprobante = serialization.deserialize(path.read_bytes())

        tfd = comprobante.get_complemento_by_type(timbre_fiscal_digitalv11.TimbreFiscalDigital)
        pagos = comprobante.get_complemento_by_type(pagos10.Pagos)

        self.assertIsInstance(tfd, timbre_fiscal_digitalv11.TimbreFiscalDigital)
        self.assertIsInstance(pagos, pagos10.Pagos)

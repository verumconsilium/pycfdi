from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional

__NAMESPACE__ = "http://www.sat.gob.mx/Pagos"


@dataclass
class Pagos:
    """Complemento para el Comprobante Fiscal Digital por Internet (CFDI) para
    registrar información sobre la recepción de pagos.

    El emisor de este complemento para recepción de pagos debe ser quien
    las leyes le obligue a expedir comprobantes por los actos o
    actividades que realicen, por los ingresos que se perciban o por las
    retenciones de contribuciones que efectúen.

    :ivar pago: Elemento requerido para incorporar la información de la
        recepción de pagos.
    :ivar version: Atributo requerido que indica la versión del
        complemento para recepción de pagos.
    """
    class Meta:
        namespace = "http://www.sat.gob.mx/Pagos"
        namespace_prefix = "pago10"

    pago: List["Pagos.Pago"] = field(
        default_factory=list,
        metadata={
            "name": "Pago",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    version: str = field(
        init=False,
        default="1.0",
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
            "white_space": "collapse",
        }
    )

    @dataclass
    class Pago:
        """
        :ivar docto_relacionado: Nodo condicional para expresar la lista
            de documentos relacionados con los pagos diferentes de
            anticipos. Por cada documento que se relacione se debe
            generar un nodo DoctoRelacionado.
        :ivar impuestos: Nodo condicional para expresar el resumen de
            los impuestos aplicables cuando este documento sea un
            anticipo.
        :ivar fecha_pago: Atributo requerido para expresar la fecha y
            hora en la que el beneficiario recibe el pago. Se expresa en
            la forma aaaa-mm-ddThh:mm:ss, de acuerdo con la
            especificación ISO 8601.En caso de no contar con la hora se
            debe registrar 12:00:00.
        :ivar forma_de_pago_p: Atributo requerido para expresar la clave
            de la forma en que se realiza el pago.
        :ivar moneda_p: Atributo requerido para identificar la clave de
            la moneda utilizada para realizar el pago, cuando se usa
            moneda nacional se registra MXN. El atributo
            Pagos:Pago:Monto y los atributos TotalImpuestosRetenidos,
            TotalImpuestosTrasladados, Traslados:Traslado:Importe y
            Retenciones:Retencion:Importe del nodo Pago:Impuestos deben
            ser expresados en esta moneda. Conforme con la
            especificación ISO 4217.
        :ivar tipo_cambio_p: Atributo condicional para expresar el tipo
            de cambio de la moneda a la fecha en que se realizó el pago.
            El valor debe reflejar el número de pesos mexicanos que
            equivalen a una unidad de la divisa señalada en el atributo
            MonedaP. Es requerido cuando el atributo MonedaP es
            diferente a MXN.
        :ivar monto: Atributo requerido para expresar el importe del
            pago.
        :ivar num_operacion: Atributo condicional para expresar el
            número de cheque, número de autorización, número de
            referencia, clave de rastreo en caso de ser SPEI, línea de
            captura o algún número de referencia análogo que identifique
            la operación que ampara el pago efectuado
        :ivar rfc_emisor_cta_ord: Atributo condicional para expresar la
            clave RFC de la entidad emisora de la cuenta origen, es
            decir, la operadora, el banco, la institución financiera,
            emisor de monedero electrónico, etc., en caso de ser
            extranjero colocar XEXX010101000, considerar las reglas de
            obligatoriedad publicadas en la página del SAT para éste
            atributo de acuerdo con el catálogo catCFDI:c_FormaPago.
        :ivar nom_banco_ord_ext: Atributo condicional para expresar el
            nombre del banco ordenante, es requerido en caso de ser
            extranjero. Considerar las reglas de obligatoriedad
            publicadas en la página del SAT para éste atributo de
            acuerdo con el catálogo catCFDI:c_FormaPago.
        :ivar cta_ordenante: Atributo condicional para incorporar el
            número de la cuenta con la que se realizó el pago.
            Considerar las reglas de obligatoriedad publicadas en la
            página del SAT para éste atributo de acuerdo con el catálogo
            catCFDI:c_FormaPago
        :ivar rfc_emisor_cta_ben: Atributo condicional para expresar la
            clave RFC de la entidad operadora de la cuenta destino, es
            decir, la operadora, el banco, la institución financiera,
            emisor de monedero electrónico, etc. Considerar las reglas
            de obligatoriedad publicadas en la página del SAT para éste
            atributo de acuerdo con el catálogo catCFDI:c_FormaPago.
        :ivar cta_beneficiario: Atributo condicional para incorporar el
            número de cuenta en donde se recibió el pago. Considerar las
            reglas de obligatoriedad publicadas en la página del SAT
            para éste atributo de acuerdo con el catálogo
            catCFDI:c_FormaPago.
        :ivar tipo_cad_pago: Atributo condicional para identificar la
            clave del tipo de cadena de pago que genera la entidad
            receptora del pago. Considerar las reglas de obligatoriedad
            publicadas en la página del SAT para éste atributo de
            acuerdo con el catálogo catCFDI:c_FormaPago.
        :ivar cert_pago: Atributo condicional que sirve para incorporar
            el certificado que ampara al pago, como una cadena de texto
            en formato base 64. Es requerido en caso de que el atributo
            TipoCadPago contenga información.
        :ivar cad_pago: Atributo condicional para expresar la cadena
            original del comprobante de pago generado por la entidad
            emisora de la cuenta beneficiaria. Es requerido en caso de
            que el atributo TipoCadPago contenga información.
        :ivar sello_pago: Atributo condicional para integrar el sello
            digital que se asocie al pago. La entidad que emite el
            comprobante de pago, ingresa una cadena original y el sello
            digital en una sección de dicho comprobante, este sello
            digital es el que se debe registrar en este campo. Debe ser
            expresado como una cadena de texto en formato base 64. Es
            requerido en caso de que el atributo TipoCadPago contenga
            información.
        """
        docto_relacionado: List["Pagos.Pago.DoctoRelacionado"] = field(
            default_factory=list,
            metadata={
                "name": "DoctoRelacionado",
                "type": "Element",
            }
        )
        impuestos: List["Pagos.Pago.Impuestos"] = field(
            default_factory=list,
            metadata={
                "name": "Impuestos",
                "type": "Element",
            }
        )
        fecha_pago: Optional[str] = field(
            default=None,
            metadata={
                "name": "FechaPago",
                "type": "Attribute",
                "required": True,
            }
        )
        forma_de_pago_p: Optional[str] = field(
            default=None,
            metadata={
                "name": "FormaDePagoP",
                "type": "Attribute",
                "required": True,
            }
        )
        moneda_p: Optional[str] = field(
            default=None,
            metadata={
                "name": "MonedaP",
                "type": "Attribute",
                "required": True,
            }
        )
        tipo_cambio_p: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "TipoCambioP",
                "type": "Attribute",
                "min_inclusive": Decimal("0.000001"),
                "fraction_digits": 6,
                "white_space": "collapse",
            }
        )
        monto: Optional[str] = field(
            default=None,
            metadata={
                "name": "Monto",
                "type": "Attribute",
                "required": True,
            }
        )
        num_operacion: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumOperacion",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 100,
                "pattern": r"[^|]{1,100}",
            }
        )
        rfc_emisor_cta_ord: Optional[str] = field(
            default=None,
            metadata={
                "name": "RfcEmisorCtaOrd",
                "type": "Attribute",
                "min_length": 12,
                "max_length": 13,
                "white_space": "collapse",
                "pattern": r"XEXX010101000|[A-Z&Ñ]{3}[0-9]{2}(0[1-9]|1[012])(0[1-9]|[12][0-9]|3[01])[A-Z0-9]{2}[0-9A]",
            }
        )
        nom_banco_ord_ext: Optional[str] = field(
            default=None,
            metadata={
                "name": "NomBancoOrdExt",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 300,
                "white_space": "collapse",
                "pattern": r"[^|]{1,300}",
            }
        )
        cta_ordenante: Optional[str] = field(
            default=None,
            metadata={
                "name": "CtaOrdenante",
                "type": "Attribute",
                "min_length": 10,
                "max_length": 50,
                "white_space": "collapse",
                "pattern": r"[A-Z0-9_]{10,50}",
            }
        )
        rfc_emisor_cta_ben: Optional[str] = field(
            default=None,
            metadata={
                "name": "RfcEmisorCtaBen",
                "type": "Attribute",
            }
        )
        cta_beneficiario: Optional[str] = field(
            default=None,
            metadata={
                "name": "CtaBeneficiario",
                "type": "Attribute",
                "min_length": 10,
                "max_length": 50,
                "white_space": "collapse",
                "pattern": r"[A-Z0-9_]{10,50}",
            }
        )
        tipo_cad_pago: Optional[str] = field(
            default=None,
            metadata={
                "name": "TipoCadPago",
                "type": "Attribute",
            }
        )
        cert_pago: Optional[bytes] = field(
            default=None,
            metadata={
                "name": "CertPago",
                "type": "Attribute",
                "white_space": "collapse",
                "format": "base64",
            }
        )
        cad_pago: Optional[str] = field(
            default=None,
            metadata={
                "name": "CadPago",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 8192,
                "white_space": "collapse",
            }
        )
        sello_pago: Optional[bytes] = field(
            default=None,
            metadata={
                "name": "SelloPago",
                "type": "Attribute",
                "white_space": "collapse",
                "format": "base64",
            }
        )

        @dataclass
        class DoctoRelacionado:
            """
            :ivar id_documento: Atributo requerido para expresar el
                identificador del documento relacionado con el pago.
                Este dato puede ser un Folio Fiscal de la Factura
                Electrónica o bien el número de operación de un
                documento digital.
            :ivar serie: Atributo opcional para precisar la serie del
                comprobante para control interno del contribuyente,
                acepta una cadena de caracteres.
            :ivar folio: Atributo opcional para precisar el folio del
                comprobante para control interno del contribuyente,
                acepta una cadena de caracteres.
            :ivar moneda_dr: Atributo requerido para identificar la
                clave de la moneda utilizada en los importes del
                documento relacionado, cuando se usa moneda nacional o
                el documento relacionado no especifica la moneda se
                registra MXN. Los importes registrados en los atributos
                “ImpSaldoAnt”, “ImpPagado” e “ImpSaldoInsoluto” de éste
                nodo, deben corresponder a esta moneda. Conforme con la
                especificación ISO 4217.
            :ivar tipo_cambio_dr: Atributo condicional para expresar el
                tipo de cambio conforme con la moneda registrada en el
                documento relacionado. Es requerido cuando la moneda del
                documento relacionado es distinta de la moneda de pago.
                Se debe registrar el número de unidades de la moneda
                señalada en el documento relacionado que equivalen a una
                unidad de la moneda del pago. Por ejemplo: El documento
                relacionado se registra en USD El pago se realiza por
                100 EUR. Este atributo se registra como 1.114700
                USD/EUR. El importe pagado equivale a 100 EUR * 1.114700
                USD/EUR = 111.47 USD.
            :ivar metodo_de_pago_dr: Atributo requerido para expresar la
                clave del método de pago que se registró en el documento
                relacionado.
            :ivar num_parcialidad: Atributo condicional para expresar el
                número de parcialidad que corresponde al pago. Es
                requerido cuando MetodoDePagoDR contiene: “PPD” Pago en
                parcialidades o diferido.
            :ivar imp_saldo_ant: Atributo condicional para expresar el
                monto del saldo insoluto de la parcialidad anterior. Es
                requerido cuando MetodoDePagoDR contiene: “PPD” Pago en
                parcialidades o diferido.En el caso de que sea la primer
                parcialidad este campo debe contener el importe total
                del documento relacionado.
            :ivar imp_pagado: Atributo condicional para expresar el
                importe pagado para el documento relacionado. Es
                obligatorio cuando exista más de un documento
                relacionado o cuando existe un documento relacionado y
                el TipoCambioDR tiene un valor.
            :ivar imp_saldo_insoluto: Atributo condicional para expresar
                la diferencia entre el importe del saldo anterior y el
                monto del pago. Es requerido cuando MetodoDePagoDR
                contiene: “PPD” Pago en parcialidades o diferido.
            """
            id_documento: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IdDocumento",
                    "type": "Attribute",
                    "required": True,
                    "min_length": 16,
                    "max_length": 36,
                    "white_space": "collapse",
                    "pattern": r"([a-f0-9A-F]{8}-[a-f0-9A-F]{4}-[a-f0-9A-F]{4}-[a-f0-9A-F]{4}-[a-f0-9A-F]{12})|([0-9]{3}-[0-9]{2}-[0-9]{9})",
                }
            )
            serie: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Serie",
                    "type": "Attribute",
                    "min_length": 1,
                    "max_length": 25,
                    "white_space": "collapse",
                    "pattern": r"[^|]{1,25}",
                }
            )
            folio: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Folio",
                    "type": "Attribute",
                    "min_length": 1,
                    "max_length": 40,
                    "white_space": "collapse",
                    "pattern": r"[^|]{1,40}",
                }
            )
            moneda_dr: Optional[str] = field(
                default=None,
                metadata={
                    "name": "MonedaDR",
                    "type": "Attribute",
                    "required": True,
                }
            )
            tipo_cambio_dr: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "TipoCambioDR",
                    "type": "Attribute",
                    "min_inclusive": Decimal("0.000001"),
                    "fraction_digits": 6,
                    "white_space": "collapse",
                }
            )
            metodo_de_pago_dr: Optional[str] = field(
                default=None,
                metadata={
                    "name": "MetodoDePagoDR",
                    "type": "Attribute",
                    "required": True,
                }
            )
            num_parcialidad: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NumParcialidad",
                    "type": "Attribute",
                    "white_space": "collapse",
                    "pattern": r"[1-9][0-9]{0,2}",
                }
            )
            imp_saldo_ant: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ImpSaldoAnt",
                    "type": "Attribute",
                }
            )
            imp_pagado: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ImpPagado",
                    "type": "Attribute",
                }
            )
            imp_saldo_insoluto: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ImpSaldoInsoluto",
                    "type": "Attribute",
                }
            )

        @dataclass
        class Impuestos:
            """
            :ivar retenciones: Nodo condicional para capturar los
                impuestos retenidos aplicables.
            :ivar traslados: Nodo condicional para capturar los
                impuestos trasladados aplicables.
            :ivar total_impuestos_retenidos: Atributo condicional para
                expresar el total de los impuestos retenidos que se
                desprenden del pago. No se permiten valores negativos.
            :ivar total_impuestos_trasladados: Atributo condicional para
                expresar el total de los impuestos trasladados que se
                desprenden del pago. No se permiten valores negativos.
            """
            retenciones: Optional["Pagos.Pago.Impuestos.Retenciones"] = field(
                default=None,
                metadata={
                    "name": "Retenciones",
                    "type": "Element",
                }
            )
            traslados: Optional["Pagos.Pago.Impuestos.Traslados"] = field(
                default=None,
                metadata={
                    "name": "Traslados",
                    "type": "Element",
                }
            )
            total_impuestos_retenidos: Optional[str] = field(
                default=None,
                metadata={
                    "name": "TotalImpuestosRetenidos",
                    "type": "Attribute",
                }
            )
            total_impuestos_trasladados: Optional[str] = field(
                default=None,
                metadata={
                    "name": "TotalImpuestosTrasladados",
                    "type": "Attribute",
                }
            )

            @dataclass
            class Retenciones:
                """
                :ivar retencion: Nodo requerido para registrar la
                    información detallada de una retención de impuesto
                    específico.
                """
                retencion: List["Pagos.Pago.Impuestos.Retenciones.Retencion"] = field(
                    default_factory=list,
                    metadata={
                        "name": "Retencion",
                        "type": "Element",
                        "min_occurs": 1,
                    }
                )

                @dataclass
                class Retencion:
                    """
                    :ivar impuesto: Atributo requerido para señalar la
                        clave del tipo de impuesto retenido.
                    :ivar importe: Atributo requerido para señalar el
                        importe o monto del impuesto retenido. No se
                        permiten valores negativos.
                    """
                    impuesto: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "Impuesto",
                            "type": "Attribute",
                            "required": True,
                        }
                    )
                    importe: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "Importe",
                            "type": "Attribute",
                            "required": True,
                        }
                    )

            @dataclass
            class Traslados:
                """
                :ivar traslado: Nodo requerido para la información
                    detallada de un traslado de impuesto específico.
                """
                traslado: List["Pagos.Pago.Impuestos.Traslados.Traslado"] = field(
                    default_factory=list,
                    metadata={
                        "name": "Traslado",
                        "type": "Element",
                        "min_occurs": 1,
                    }
                )

                @dataclass
                class Traslado:
                    """
                    :ivar impuesto: Atributo requerido para señalar la
                        clave del tipo de impuesto trasladado.
                    :ivar tipo_factor: Atributo requerido para señalar
                        la clave del tipo de factor que se aplica a la
                        base del impuesto.
                    :ivar tasa_ocuota: Atributo requerido para señalar
                        el valor de la tasa o cuota del impuesto que se
                        traslada.
                    :ivar importe: Atributo requerido para señalar el
                        importe del impuesto trasladado. No se permiten
                        valores negativos.
                    """
                    impuesto: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "Impuesto",
                            "type": "Attribute",
                            "required": True,
                        }
                    )
                    tipo_factor: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "TipoFactor",
                            "type": "Attribute",
                            "required": True,
                        }
                    )
                    tasa_ocuota: Optional[Decimal] = field(
                        default=None,
                        metadata={
                            "name": "TasaOCuota",
                            "type": "Attribute",
                            "required": True,
                            "min_inclusive": Decimal("0.000000"),
                            "fraction_digits": 6,
                            "white_space": "collapse",
                        }
                    )
                    importe: Optional[str] = field(
                        default=None,
                        metadata={
                            "name": "Importe",
                            "type": "Attribute",
                            "required": True,
                        }
                    )

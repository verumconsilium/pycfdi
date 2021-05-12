from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "http://www.sat.gob.mx/nomina12"


class ReceptorSindicalizado(Enum):
    SI = "Sí"
    NO = "No"


@dataclass
class Nomina:
    """
    Complemento para incorporar al Comprobante Fiscal Digital por Internet
    (CFDI) la información que ampara conceptos de ingresos por salarios, la
    prestación de un servicio personal subordinado o conceptos asimilados a
    salarios (Nómina).

    :ivar emisor: Nodo condicional para expresar la información del
        contribuyente emisor del comprobante de nómina.
    :ivar receptor: Nodo requerido para precisar la información del
        contribuyente receptor del comprobante de nómina.
    :ivar percepciones: Nodo condicional para expresar las percepciones
        aplicables.
    :ivar deducciones: Nodo opcional para expresar las deducciones
        aplicables.
    :ivar otros_pagos: Nodo condicional para expresar otros pagos
        aplicables.
    :ivar incapacidades: Nodo condicional para expresar información de
        las incapacidades.
    :ivar version: Atributo requerido para la expresión de la versión
        del complemento.
    :ivar tipo_nomina: Atributo requerido para indicar el tipo de
        nómina, puede ser O= Nómina ordinaria o E= Nómina
        extraordinaria.
    :ivar fecha_pago: Atributo requerido para la expresión de la fecha
        efectiva de erogación del gasto. Se expresa en la forma aaaa-mm-
        dd, de acuerdo con la especificación ISO 8601.
    :ivar fecha_inicial_pago: Atributo requerido para la expresión de la
        fecha inicial del período de pago. Se expresa en la forma aaaa-
        mm-dd, de acuerdo con la especificación ISO 8601.
    :ivar fecha_final_pago: Atributo requerido para la expresión de la
        fecha final del período de pago. Se expresa en la forma aaaa-mm-
        dd, de acuerdo con la especificación ISO 8601.
    :ivar num_dias_pagados: Atributo requerido para la expresión del
        número o la fracción de días pagados.
    :ivar total_percepciones: Atributo condicional para representar la
        suma de las percepciones.
    :ivar total_deducciones: Atributo condicional para representar la
        suma de las deducciones aplicables.
    :ivar total_otros_pagos: Atributo condicional para representar la
        suma de otros pagos.
    """
    class Meta:
        namespace = "http://www.sat.gob.mx/nomina12"
        namespace_prefix = "nomina12"
        schema_location = "http://www.sat.gob.mx/sitio_internet/cfd/nomina/nomina12.xsd"

    emisor: Optional["Nomina.Emisor"] = field(
        default=None,
        metadata={
            "name": "Emisor",
            "type": "Element",
        }
    )
    receptor: Optional["Nomina.Receptor"] = field(
        default=None,
        metadata={
            "name": "Receptor",
            "type": "Element",
            "required": True,
        }
    )
    percepciones: Optional["Nomina.Percepciones"] = field(
        default=None,
        metadata={
            "name": "Percepciones",
            "type": "Element",
        }
    )
    deducciones: Optional["Nomina.Deducciones"] = field(
        default=None,
        metadata={
            "name": "Deducciones",
            "type": "Element",
        }
    )
    otros_pagos: Optional["Nomina.OtrosPagos"] = field(
        default=None,
        metadata={
            "name": "OtrosPagos",
            "type": "Element",
        }
    )
    incapacidades: Optional["Nomina.Incapacidades"] = field(
        default=None,
        metadata={
            "name": "Incapacidades",
            "type": "Element",
        }
    )
    version: str = field(
        init=False,
        default="1.2",
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )
    tipo_nomina: Optional[str] = field(
        default=None,
        metadata={
            "name": "TipoNomina",
            "type": "Attribute",
            "required": True,
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
    fecha_inicial_pago: Optional[str] = field(
        default=None,
        metadata={
            "name": "FechaInicialPago",
            "type": "Attribute",
            "required": True,
        }
    )
    fecha_final_pago: Optional[str] = field(
        default=None,
        metadata={
            "name": "FechaFinalPago",
            "type": "Attribute",
            "required": True,
        }
    )
    num_dias_pagados: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumDiasPagados",
            "type": "Attribute",
            "required": True,
            "min_inclusive": "0.001",
            "max_inclusive": "36160.000",
            "fraction_digits": 3,
            "white_space": "collapse",
            "pattern": r"(([1-9][0-9]{0,4})|[0])(.[0-9]{3})?",
        }
    )
    total_percepciones: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalPercepciones",
            "type": "Attribute",
        }
    )
    total_deducciones: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalDeducciones",
            "type": "Attribute",
        }
    )
    total_otros_pagos: Optional[str] = field(
        default=None,
        metadata={
            "name": "TotalOtrosPagos",
            "type": "Attribute",
        }
    )

    @dataclass
    class Emisor:
        """
        :ivar entidad_sncf: Nodo condicional para que las entidades
            adheridas al Sistema Nacional de Coordinación Fiscal
            realicen la identificación del origen de los recursos
            utilizados en el pago de nómina del personal que presta o
            desempeña un servicio personal subordinado en las
            dependencias de la entidad federativa, del municipio o
            demarcación territorial de la Ciudad de México, así como en
            sus respectivos organismos autónomos y entidades
            paraestatales y paramunicipales
        :ivar curp: Atributo condicional para expresar la CURP del
            emisor del comprobante de nómina cuando es una persona
            física.
        :ivar registro_patronal: Atributo condicional para expresar el
            registro patronal, clave de ramo - pagaduría o la que le
            asigne la institución de seguridad social al patrón, a 20
            posiciones máximo. Se debe ingresar cuando se cuente con él,
            o se esté obligado conforme a otras disposiciones distintas
            a las fiscales.
        :ivar rfc_patron_origen: Atributo opcional para expresar el RFC
            de la persona que fungió como patrón cuando el pago al
            trabajador se realice a través de un tercero como vehículo o
            herramienta de pago.
        """
        entidad_sncf: Optional["Nomina.Emisor.EntidadSncf"] = field(
            default=None,
            metadata={
                "name": "EntidadSNCF",
                "type": "Element",
            }
        )
        curp: Optional[str] = field(
            default=None,
            metadata={
                "name": "Curp",
                "type": "Attribute",
            }
        )
        registro_patronal: Optional[str] = field(
            default=None,
            metadata={
                "name": "RegistroPatronal",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 20,
                "white_space": "collapse",
                "pattern": r"[^|]{1,20}",
            }
        )
        rfc_patron_origen: Optional[str] = field(
            default=None,
            metadata={
                "name": "RfcPatronOrigen",
                "type": "Attribute",
            }
        )

        @dataclass
        class EntidadSncf:
            """
            :ivar origen_recurso: Atributo requerido para identificar el
                origen del recurso utilizado para el pago de nómina del
                personal que presta o desempeña un servicio personal
                subordinado o asimilado a salarios en las dependencias.
            :ivar monto_recurso_propio: Atributo condicional para
                expresar el monto del recurso pagado con cargo a sus
                participaciones u otros ingresos locales (importe bruto
                de los ingresos propios, es decir total de gravados y
                exentos), cuando el origen es mixto.
            """
            origen_recurso: Optional[str] = field(
                default=None,
                metadata={
                    "name": "OrigenRecurso",
                    "type": "Attribute",
                    "required": True,
                }
            )
            monto_recurso_propio: Optional[str] = field(
                default=None,
                metadata={
                    "name": "MontoRecursoPropio",
                    "type": "Attribute",
                }
            )

    @dataclass
    class Receptor:
        """
        :ivar sub_contratacion: Nodo condicional para expresar la lista
            de las personas que los subcontrataron.
        :ivar curp: Atributo requerido para expresar la CURP del
            receptor del comprobante de nómina.
        :ivar num_seguridad_social: Atributo condicional para expresar
            el número de seguridad social del trabajador. Se debe
            ingresar cuando se cuente con él, o se esté obligado
            conforme a otras disposiciones distintas a las fiscales.
        :ivar fecha_inicio_rel_laboral: Atributo condicional para
            expresar la fecha de inicio de la relación laboral entre el
            empleador y el empleado. Se expresa en la forma aaaa-mm-dd,
            de acuerdo con la especificación ISO 8601. Se debe ingresar
            cuando se cuente con él, o se esté obligado conforme a otras
            disposiciones distintas a las fiscales.
        :ivar antig_edad: Atributo condicional para expresar el número
            de semanas o el periodo de años, meses y días que el
            empleado ha mantenido relación laboral con el empleador. Se
            debe ingresar cuando se cuente con él, o se esté obligado
            conforme a otras disposiciones distintas a las fiscales.
        :ivar tipo_contrato: Atributo requerido para expresar el tipo de
            contrato que tiene el trabajador.
        :ivar sindicalizado: Atributo opcional para indicar si el
            trabajador está asociado a un sindicato. Si se omite se
            asume que no está asociado a algún sindicato.
        :ivar tipo_jornada: Atributo condicional para expresar el tipo
            de jornada que cubre el trabajador. Se debe ingresar cuando
            se esté obligado conforme a otras disposiciones distintas a
            las fiscales.
        :ivar tipo_regimen: Atributo requerido para la expresión de la
            clave del régimen por el cual se tiene contratado al
            trabajador.
        :ivar num_empleado: Atributo requerido para expresar el número
            de empleado de 1 a 15 posiciones.
        :ivar departamento: Atributo opcional para la expresión del
            departamento o área a la que pertenece el trabajador.
        :ivar puesto: Atributo opcional para la expresión del puesto
            asignado al empleado o actividad que realiza.
        :ivar riesgo_puesto: Atributo opcional para expresar la clave
            conforme a la Clase en que deben inscribirse los patrones,
            de acuerdo con las actividades que desempeñan sus
            trabajadores, según lo previsto en el artículo 196 del
            Reglamento en Materia de Afiliación Clasificación de
            Empresas, Recaudación y Fiscalización, o conforme con la
            normatividad del Instituto de Seguridad Social del
            trabajador.  Se debe ingresar cuando se cuente con él, o se
            esté obligado conforme a otras disposiciones distintas a las
            fiscales.
        :ivar periodicidad_pago: Atributo requerido para la forma en que
            se establece el pago del salario.
        :ivar banco: Atributo condicional para la expresión de la clave
            del Banco conforme al catálogo, donde se realiza el depósito
            de nómina.
        :ivar cuenta_bancaria: Atributo condicional para la expresión de
            la cuenta bancaria a 11 posiciones o número de teléfono
            celular a 10 posiciones o número de tarjeta de crédito,
            débito o servicios a 15 ó 16 posiciones o la CLABE a 18
            posiciones o número de monedero electrónico, donde se
            realiza el depósito de nómina.
        :ivar salario_base_cot_apor: Atributo opcional para expresar la
            retribución otorgada al trabajador, que se integra por los
            pagos hechos en efectivo por cuota diaria, gratificaciones,
            percepciones, alimentación, habitación, primas, comisiones,
            prestaciones en especie y cualquiera otra cantidad o
            prestación que se entregue al trabajador por su trabajo, sin
            considerar los conceptos que se excluyen de conformidad con
            el Artículo 27 de la Ley del Seguro Social, o la integración
            de los pagos conforme la normatividad del Instituto de
            Seguridad Social del trabajador. (Se emplea para pagar las
            cuotas y aportaciones de Seguridad Social). Se debe ingresar
            cuando se esté obligado conforme a otras disposiciones
            distintas a las fiscales.
        :ivar salario_diario_integrado: Atributo opcional para expresar
            el salario que se integra con los pagos hechos en efectivo
            por cuota diaria, gratificaciones, percepciones, habitación,
            primas, comisiones, prestaciones en especie y cualquier otra
            cantidad o prestación que se entregue al trabajador por su
            trabajo, de conformidad con el Art. 84 de la Ley Federal del
            Trabajo. (Se utiliza para el cálculo de las
            indemnizaciones). Se debe ingresar cuando se esté obligado
            conforme a otras disposiciones distintas a las fiscales.
        :ivar clave_ent_fed: Atributo requerido para expresar la clave
            de la entidad federativa en donde el receptor del recibo
            prestó el servicio.
        """
        sub_contratacion: List["Nomina.Receptor.SubContratacion"] = field(
            default_factory=list,
            metadata={
                "name": "SubContratacion",
                "type": "Element",
            }
        )
        curp: Optional[str] = field(
            default=None,
            metadata={
                "name": "Curp",
                "type": "Attribute",
                "required": True,
            }
        )
        num_seguridad_social: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumSeguridadSocial",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 15,
                "white_space": "collapse",
                "pattern": r"[0-9]{1,15}",
            }
        )
        fecha_inicio_rel_laboral: Optional[str] = field(
            default=None,
            metadata={
                "name": "FechaInicioRelLaboral",
                "type": "Attribute",
            }
        )
        antig_edad: Optional[str] = field(
            default=None,
            metadata={
                "name": "Antigüedad",
                "type": "Attribute",
                "white_space": "collapse",
                "pattern": r"P(([1-9][0-9]{0,3})|0)W|P([1-9][0-9]?Y)?(([1-9]|1[012])M)?(0|[1-9]|[12][0-9]|3[01])D",
            }
        )
        tipo_contrato: Optional[str] = field(
            default=None,
            metadata={
                "name": "TipoContrato",
                "type": "Attribute",
                "required": True,
            }
        )
        sindicalizado: Optional[ReceptorSindicalizado] = field(
            default=None,
            metadata={
                "name": "Sindicalizado",
                "type": "Attribute",
                "white_space": "collapse",
            }
        )
        tipo_jornada: Optional[str] = field(
            default=None,
            metadata={
                "name": "TipoJornada",
                "type": "Attribute",
            }
        )
        tipo_regimen: Optional[str] = field(
            default=None,
            metadata={
                "name": "TipoRegimen",
                "type": "Attribute",
                "required": True,
            }
        )
        num_empleado: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumEmpleado",
                "type": "Attribute",
                "required": True,
                "min_length": 1,
                "max_length": 15,
                "white_space": "collapse",
                "pattern": r"[^|]{1,15}",
            }
        )
        departamento: Optional[str] = field(
            default=None,
            metadata={
                "name": "Departamento",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 100,
                "white_space": "collapse",
                "pattern": r"[^|]{1,100}",
            }
        )
        puesto: Optional[str] = field(
            default=None,
            metadata={
                "name": "Puesto",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 100,
                "white_space": "collapse",
                "pattern": r"[^|]{1,100}",
            }
        )
        riesgo_puesto: Optional[str] = field(
            default=None,
            metadata={
                "name": "RiesgoPuesto",
                "type": "Attribute",
            }
        )
        periodicidad_pago: Optional[str] = field(
            default=None,
            metadata={
                "name": "PeriodicidadPago",
                "type": "Attribute",
                "required": True,
            }
        )
        banco: Optional[str] = field(
            default=None,
            metadata={
                "name": "Banco",
                "type": "Attribute",
            }
        )
        cuenta_bancaria: Optional[str] = field(
            default=None,
            metadata={
                "name": "CuentaBancaria",
                "type": "Attribute",
            }
        )
        salario_base_cot_apor: Optional[str] = field(
            default=None,
            metadata={
                "name": "SalarioBaseCotApor",
                "type": "Attribute",
            }
        )
        salario_diario_integrado: Optional[str] = field(
            default=None,
            metadata={
                "name": "SalarioDiarioIntegrado",
                "type": "Attribute",
            }
        )
        clave_ent_fed: Optional[str] = field(
            default=None,
            metadata={
                "name": "ClaveEntFed",
                "type": "Attribute",
                "required": True,
            }
        )

        @dataclass
        class SubContratacion:
            """
            :ivar rfc_labora: Atributo requerido para expresar el RFC de
                la persona que subcontrata.
            :ivar porcentaje_tiempo: Atributo requerido para expresar el
                porcentaje del tiempo que prestó sus servicios con el
                RFC que lo subcontrata.
            """
            rfc_labora: Optional[str] = field(
                default=None,
                metadata={
                    "name": "RfcLabora",
                    "type": "Attribute",
                    "required": True,
                }
            )
            porcentaje_tiempo: Optional[str] = field(
                default=None,
                metadata={
                    "name": "PorcentajeTiempo",
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": "0.001",
                    "max_inclusive": "100.000",
                    "white_space": "collapse",
                    "pattern": r"[0-9]{1,3}(.([0-9]{1,3}))?",
                }
            )

    @dataclass
    class Percepciones:
        """
        :ivar percepcion: Nodo requerido para expresar la información
            detallada de una percepción
        :ivar jubilacion_pension_retiro: Nodo condicional para expresar
            la información detallada de pagos por jubilación, pensiones
            o haberes de retiro.
        :ivar separacion_indemnizacion: Nodo condicional para expresar
            la información detallada de otros pagos por separación.
        :ivar total_sueldos: Atributo condicional para expresar el total
            de percepciones brutas (gravadas y exentas) por sueldos y
            salarios y conceptos asimilados a salarios.
        :ivar total_separacion_indemnizacion: Atributo condicional para
            expresar el importe exento y gravado de las claves tipo
            percepción 022 Prima por Antigüedad, 023 Pagos por
            separación y 025 Indemnizaciones.
        :ivar total_jubilacion_pension_retiro: Atributo condicional para
            expresar el importe exento y gravado de las claves tipo
            percepción 039 Jubilaciones, pensiones o haberes de retiro
            en una exhibición y 044 Jubilaciones, pensiones o haberes de
            retiro en parcialidades.
        :ivar total_gravado: Atributo requerido para expresar el total
            de percepciones gravadas que se relacionan en el
            comprobante.
        :ivar total_exento: Atributo requerido para expresar el total de
            percepciones exentas que se relacionan en el comprobante.
        """
        percepcion: List["Nomina.Percepciones.Percepcion"] = field(
            default_factory=list,
            metadata={
                "name": "Percepcion",
                "type": "Element",
                "min_occurs": 1,
            }
        )
        jubilacion_pension_retiro: Optional["Nomina.Percepciones.JubilacionPensionRetiro"] = field(
            default=None,
            metadata={
                "name": "JubilacionPensionRetiro",
                "type": "Element",
            }
        )
        separacion_indemnizacion: Optional["Nomina.Percepciones.SeparacionIndemnizacion"] = field(
            default=None,
            metadata={
                "name": "SeparacionIndemnizacion",
                "type": "Element",
            }
        )
        total_sueldos: Optional[str] = field(
            default=None,
            metadata={
                "name": "TotalSueldos",
                "type": "Attribute",
            }
        )
        total_separacion_indemnizacion: Optional[str] = field(
            default=None,
            metadata={
                "name": "TotalSeparacionIndemnizacion",
                "type": "Attribute",
            }
        )
        total_jubilacion_pension_retiro: Optional[str] = field(
            default=None,
            metadata={
                "name": "TotalJubilacionPensionRetiro",
                "type": "Attribute",
            }
        )
        total_gravado: Optional[str] = field(
            default=None,
            metadata={
                "name": "TotalGravado",
                "type": "Attribute",
                "required": True,
            }
        )
        total_exento: Optional[str] = field(
            default=None,
            metadata={
                "name": "TotalExento",
                "type": "Attribute",
                "required": True,
            }
        )

        @dataclass
        class Percepcion:
            """
            :ivar acciones_otitulos: Nodo condicional para expresar
                ingresos por acciones o títulos valor que representan
                bienes. Se vuelve requerido cuando existan ingresos por
                sueldos derivados de adquisición de acciones o títulos
                (Art. 94, fracción VII LISR).
            :ivar horas_extra: Nodo condicional para expresar las horas
                extra aplicables.
            :ivar tipo_percepcion: Atributo requerido para expresar la
                Clave agrupadora bajo la cual se clasifica la
                percepción.
            :ivar clave: Atributo requerido para expresar la clave de
                percepción de nómina propia de la contabilidad de cada
                patrón, puede conformarse desde 3 hasta 15 caracteres.
            :ivar concepto: Atributo requerido para la descripción del
                concepto de percepción
            :ivar importe_gravado: Atributo requerido, representa el
                importe gravado de un concepto de percepción.
            :ivar importe_exento: Atributo requerido, representa el
                importe exento de un concepto de percepción.
            """
            acciones_otitulos: Optional["Nomina.Percepciones.Percepcion.AccionesOtitulos"] = field(
                default=None,
                metadata={
                    "name": "AccionesOTitulos",
                    "type": "Element",
                }
            )
            horas_extra: List["Nomina.Percepciones.Percepcion.HorasExtra"] = field(
                default_factory=list,
                metadata={
                    "name": "HorasExtra",
                    "type": "Element",
                }
            )
            tipo_percepcion: Optional[str] = field(
                default=None,
                metadata={
                    "name": "TipoPercepcion",
                    "type": "Attribute",
                    "required": True,
                }
            )
            clave: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Clave",
                    "type": "Attribute",
                    "required": True,
                    "min_length": 3,
                    "max_length": 15,
                    "white_space": "collapse",
                    "pattern": r"[^|]{3,15}",
                }
            )
            concepto: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Concepto",
                    "type": "Attribute",
                    "required": True,
                    "min_length": 1,
                    "max_length": 100,
                    "white_space": "collapse",
                    "pattern": r"[^|]{1,100}",
                }
            )
            importe_gravado: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ImporteGravado",
                    "type": "Attribute",
                    "required": True,
                }
            )
            importe_exento: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ImporteExento",
                    "type": "Attribute",
                    "required": True,
                }
            )

            @dataclass
            class AccionesOtitulos:
                """
                :ivar valor_mercado: Atributo requerido para expresar el
                    valor de mercado de las Acciones o Títulos valor al
                    ejercer la opción.
                :ivar precio_al_otorgarse: Atributo requerido para
                    expresar el precio establecido al otorgarse la
                    opción de ingresos en acciones o títulos valor.
                """
                valor_mercado: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "ValorMercado",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": Decimal("0.000001"),
                        "fraction_digits": 6,
                        "white_space": "collapse",
                    }
                )
                precio_al_otorgarse: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "PrecioAlOtorgarse",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": Decimal("0.000001"),
                        "fraction_digits": 6,
                        "white_space": "collapse",
                    }
                )

            @dataclass
            class HorasExtra:
                """
                :ivar dias: Atributo requerido para expresar el número
                    de días en que el trabajador realizó horas extra en
                    el periodo.
                :ivar tipo_horas: Atributo requerido para expresar el
                    tipo de pago de las horas extra.
                :ivar horas_extra: Atributo requerido para expresar el
                    número de horas extra trabajadas en el periodo.
                :ivar importe_pagado: Atributo requerido para expresar
                    el importe pagado por las horas extra.
                """
                dias: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Dias",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 1,
                        "white_space": "collapse",
                    }
                )
                tipo_horas: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "TipoHoras",
                        "type": "Attribute",
                        "required": True,
                    }
                )
                horas_extra: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "HorasExtra",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 1,
                        "white_space": "collapse",
                    }
                )
                importe_pagado: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "ImportePagado",
                        "type": "Attribute",
                        "required": True,
                    }
                )

        @dataclass
        class JubilacionPensionRetiro:
            """
            :ivar total_una_exhibicion: Atributo condicional que indica
                el monto total del pago cuando se realiza en una sola
                exhibición.
            :ivar total_parcialidad: Atributo condicional para expresar
                los ingresos totales por pago cuando se hace en
                parcialidades.
            :ivar monto_diario: Atributo condicional para expresar el
                monto diario percibido por jubilación, pensiones o
                haberes de retiro cuando se realiza en parcialidades.
            :ivar ingreso_acumulable: Atributo requerido para expresar
                los ingresos acumulables.
            :ivar ingreso_no_acumulable: Atributo requerido para
                expresar los ingresos no acumulables.
            """
            total_una_exhibicion: Optional[str] = field(
                default=None,
                metadata={
                    "name": "TotalUnaExhibicion",
                    "type": "Attribute",
                }
            )
            total_parcialidad: Optional[str] = field(
                default=None,
                metadata={
                    "name": "TotalParcialidad",
                    "type": "Attribute",
                }
            )
            monto_diario: Optional[str] = field(
                default=None,
                metadata={
                    "name": "MontoDiario",
                    "type": "Attribute",
                }
            )
            ingreso_acumulable: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IngresoAcumulable",
                    "type": "Attribute",
                    "required": True,
                }
            )
            ingreso_no_acumulable: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IngresoNoAcumulable",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass
        class SeparacionIndemnizacion:
            """
            :ivar total_pagado: Atributo requerido que indica el monto
                total del pago.
            :ivar num_a_os_servicio: Atributo requerido para expresar el
                número de años de servicio del trabajador. Se redondea
                al entero superior si la cifra contiene años y meses y
                hay más de 6 meses.
            :ivar ultimo_sueldo_mens_ord: Atributo requerido que indica
                el último sueldo mensual ordinario.
            :ivar ingreso_acumulable: Atributo requerido para expresar
                los ingresos acumulables.
            :ivar ingreso_no_acumulable: Atributo requerido que indica
                los ingresos no acumulables.
            """
            total_pagado: Optional[str] = field(
                default=None,
                metadata={
                    "name": "TotalPagado",
                    "type": "Attribute",
                    "required": True,
                }
            )
            num_a_os_servicio: Optional[int] = field(
                default=None,
                metadata={
                    "name": "NumAñosServicio",
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 0,
                    "max_inclusive": 99,
                    "white_space": "collapse",
                }
            )
            ultimo_sueldo_mens_ord: Optional[str] = field(
                default=None,
                metadata={
                    "name": "UltimoSueldoMensOrd",
                    "type": "Attribute",
                    "required": True,
                }
            )
            ingreso_acumulable: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IngresoAcumulable",
                    "type": "Attribute",
                    "required": True,
                }
            )
            ingreso_no_acumulable: Optional[str] = field(
                default=None,
                metadata={
                    "name": "IngresoNoAcumulable",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class Deducciones:
        """
        :ivar deduccion: Nodo requerido para expresar la información
            detallada de una deducción.
        :ivar total_otras_deducciones: Atributo condicional para
            expresar el total de deducciones que se relacionan en el
            comprobante, donde la clave de tipo de deducción sea
            distinta a la 002 correspondiente a ISR.
        :ivar total_impuestos_retenidos: Atributo condicional para
            expresar el total de los impuestos federales retenidos, es
            decir, donde la clave de tipo de deducción sea 002
            correspondiente a ISR.
        """
        deduccion: List["Nomina.Deducciones.Deduccion"] = field(
            default_factory=list,
            metadata={
                "name": "Deduccion",
                "type": "Element",
                "min_occurs": 1,
            }
        )
        total_otras_deducciones: Optional[str] = field(
            default=None,
            metadata={
                "name": "TotalOtrasDeducciones",
                "type": "Attribute",
            }
        )
        total_impuestos_retenidos: Optional[str] = field(
            default=None,
            metadata={
                "name": "TotalImpuestosRetenidos",
                "type": "Attribute",
            }
        )

        @dataclass
        class Deduccion:
            """
            :ivar tipo_deduccion: Atributo requerido para registrar la
                clave agrupadora que clasifica la deducción.
            :ivar clave: Atributo requerido para la clave de deducción
                de nómina propia de la contabilidad de cada patrón,
                puede conformarse desde 3 hasta 15 caracteres.
            :ivar concepto: Atributo requerido para la descripción del
                concepto de deducción.
            :ivar importe: Atributo requerido para registrar el importe
                del concepto de deducción.
            """
            tipo_deduccion: Optional[str] = field(
                default=None,
                metadata={
                    "name": "TipoDeduccion",
                    "type": "Attribute",
                    "required": True,
                }
            )
            clave: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Clave",
                    "type": "Attribute",
                    "required": True,
                    "min_length": 3,
                    "max_length": 15,
                    "pattern": r"[^|]{3,15}",
                }
            )
            concepto: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Concepto",
                    "type": "Attribute",
                    "required": True,
                    "min_length": 1,
                    "max_length": 100,
                    "pattern": r"[^|]{1,100}",
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
    class OtrosPagos:
        """
        :ivar otro_pago: Nodo requerido para expresar la información
            detallada del otro pago.
        """
        otro_pago: List["Nomina.OtrosPagos.OtroPago"] = field(
            default_factory=list,
            metadata={
                "name": "OtroPago",
                "type": "Element",
                "min_occurs": 1,
            }
        )

        @dataclass
        class OtroPago:
            """
            :ivar subsidio_al_empleo: Nodo condicional para expresar la
                información referente al subsidio al empleo del
                trabajador.
            :ivar compensacion_saldos_afavor: Nodo condicional para
                expresar la información referente a la compensación de
                saldos a favor de un trabajador.
            :ivar tipo_otro_pago: Atributo requerido para expresar la
                clave agrupadora bajo la cual se clasifica el otro pago.
            :ivar clave: Atributo requerido, representa la clave de otro
                pago de nómina propia de la contabilidad de cada patrón,
                puede conformarse desde 3 hasta 15 caracteres.
            :ivar concepto: Atributo requerido para la descripción del
                concepto de otro pago.
            :ivar importe: Atributo requerido para expresar el importe
                del concepto de otro pago.
            """
            subsidio_al_empleo: Optional["Nomina.OtrosPagos.OtroPago.SubsidioAlEmpleo"] = field(
                default=None,
                metadata={
                    "name": "SubsidioAlEmpleo",
                    "type": "Element",
                }
            )
            compensacion_saldos_afavor: Optional["Nomina.OtrosPagos.OtroPago.CompensacionSaldosAfavor"] = field(
                default=None,
                metadata={
                    "name": "CompensacionSaldosAFavor",
                    "type": "Element",
                }
            )
            tipo_otro_pago: Optional[str] = field(
                default=None,
                metadata={
                    "name": "TipoOtroPago",
                    "type": "Attribute",
                    "required": True,
                }
            )
            clave: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Clave",
                    "type": "Attribute",
                    "required": True,
                    "min_length": 3,
                    "max_length": 15,
                    "white_space": "collapse",
                    "pattern": r"[^|]{3,15}",
                }
            )
            concepto: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Concepto",
                    "type": "Attribute",
                    "required": True,
                    "min_length": 1,
                    "max_length": 100,
                    "white_space": "collapse",
                    "pattern": r"[^|]{1,100}",
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
            class SubsidioAlEmpleo:
                """
                :ivar subsidio_causado: Atributo requerido para expresar
                    el subsidio causado conforme a la tabla del subsidio
                    para el empleo publicada en el Anexo 8 de la RMF
                    vigente.
                """
                subsidio_causado: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "SubsidioCausado",
                        "type": "Attribute",
                        "required": True,
                    }
                )

            @dataclass
            class CompensacionSaldosAfavor:
                """
                :ivar saldo_afavor: Atributo requerido para expresar el
                    saldo a favor determinado por el patrón al
                    trabajador en periodos o ejercicios anteriores.
                :ivar a_o: Atributo requerido para expresar el año en
                    que se determinó el saldo a favor del trabajador por
                    el patrón que se incluye en el campo
                    “RemanenteSalFav”.
                :ivar remanente_sal_fav: Atributo requerido para
                    expresar el remanente del saldo a favor del
                    trabajador.
                """
                saldo_afavor: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "SaldoAFavor",
                        "type": "Attribute",
                        "required": True,
                    }
                )
                a_o: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "Año",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 2016,
                        "white_space": "collapse",
                    }
                )
                remanente_sal_fav: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "RemanenteSalFav",
                        "type": "Attribute",
                        "required": True,
                    }
                )

    @dataclass
    class Incapacidades:
        """
        :ivar incapacidad: Nodo requerido para expresar información de
            las incapacidades.
        """
        incapacidad: List["Nomina.Incapacidades.Incapacidad"] = field(
            default_factory=list,
            metadata={
                "name": "Incapacidad",
                "type": "Element",
                "min_occurs": 1,
            }
        )

        @dataclass
        class Incapacidad:
            """
            :ivar dias_incapacidad: Atributo requerido para expresar el
                número de días enteros que el trabajador se incapacitó
                en el periodo.
            :ivar tipo_incapacidad: Atributo requerido para expresar la
                razón de la incapacidad.
            :ivar importe_monetario: Atributo condicional para expresar
                el monto del importe monetario de la incapacidad.
            """
            dias_incapacidad: Optional[int] = field(
                default=None,
                metadata={
                    "name": "DiasIncapacidad",
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 1,
                    "white_space": "collapse",
                }
            )
            tipo_incapacidad: Optional[str] = field(
                default=None,
                metadata={
                    "name": "TipoIncapacidad",
                    "type": "Attribute",
                    "required": True,
                }
            )
            importe_monetario: Optional[str] = field(
                default=None,
                metadata={
                    "name": "ImporteMonetario",
                    "type": "Attribute",
                }
            )

from dataclasses import is_dataclass
from lxml import etree
from pathlib import Path
from typing import Union, Optional, Type, TypeVar, Callable
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig
from xsdata.formats.dataclass.parsers import XmlParser
import os.path

T = TypeVar("T")


def serialize(obj: object) -> str:
    ns_map = __get_ns_map(obj)
    schema_location = __get_ns_schema_location(obj)
    config = SerializerConfig(
        xml_version='1.0',
        encoding='UTF-8',
        schema_location=schema_location,
        pretty_print=True
    )
    serializer = XmlSerializer(config=config)

    return serializer.render(obj, ns_map=ns_map)


def deserialize(resource: Union[str, Path, bytes], target_class: Optional[Type[T]] = None) -> Optional[T]:
    parser = XmlParser(context=XmlContext())
    obj = None

    if os.path.isfile(resource):
        resource = Path(resource)
        pass

    if isinstance(resource, str):
        obj = parser.from_string(resource, target_class)
    if isinstance(resource, Path):
        obj = parser.from_path(resource, target_class)
    if isinstance(resource, bytes):
        obj = parser.from_bytes(resource, target_class)

    return obj


def cadena_original(obj: Union[object, str, bytes, Path], xslt: Union[str, Path, bytes] = None) -> str:
    if not xslt and hasattr(obj, 'Meta') and hasattr(obj.Meta, 'stylesheet'):
        xslt = obj.Meta.stylesheet

    if not xslt:
        raise ValueError('XSLT was not provided nor could it be found automatically for the object.')

    xslt_root = __get_element_tree(xslt)
    xml_root = __get_element_tree(obj)

    transform = __get_xslt_transform(xslt_root)
    result = transform(xml_root)

    return str(result)


def __get_ns_map(obj: object) -> dict:
    meta_classes = __get_meta_classes(obj)
    ns_map = {}

    for meta in meta_classes:
        ns_map[getattr(meta, 'namespace_prefix', None)] = getattr(meta, 'namespace', None)

    return ns_map


def __get_ns_schema_location(obj: object) -> str:
    meta_classes = __get_meta_classes(obj)
    schema_locations = [
        getattr(meta, 'namespace', '') + ' ' + getattr(meta, 'schema_location', '')
        for meta in meta_classes
    ]

    return ' '.join(schema_locations)


def __get_meta_classes(obj: object) -> list:
    meta_classes = []
    if hasattr(obj, 'Meta'):
        meta_classes.append(obj.Meta)

    if hasattr(obj, 'complemento') \
            and hasattr(obj.complemento, 'any_element') \
            and isinstance(obj.complemento.any_element, list):
        meta_classes += [getattr(x, 'Meta') for x in obj.complemento.any_element if hasattr(x, 'Meta')]

    return meta_classes


def __get_xslt_transform(xslt_root: etree.ElementTree) -> etree.XSLT:
    return etree.XSLT(xslt_root)


def __get_element_tree(source: Union[str, Path, bytes, object, Callable]) -> etree.ElementTree:
    if isinstance(source, Callable):
        source = source()

    if isinstance(source, str):
        import validators
        if validators.url(source):
            return etree.parse(source)

        return etree.XML(source.encode())
    if isinstance(source, Path):
        return etree.parse(str(source))
    if isinstance(source, bytes):
        from io import BytesIO
        return etree.parse(BytesIO(source))
    if is_dataclass(source):
        return etree.XML(serialize(source).encode())

    return None

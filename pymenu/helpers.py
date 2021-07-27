from __future__ import annotations
import typing as t


def protect(*protected) -> t.Type[Protect]:
    """Returns a metaclass that protects all attributes given as strings"""
    class Protect(type):
        has_base = False

        def __new__(meta, name, bases, attrs):
            if meta.has_base:
                for attribute in attrs:
                    if attribute in protected:
                        raise AttributeError(
                            f'Overriding of attribute "{attribute}" not allowed.')
            meta.has_base = True
            klass = super().__new__(meta, name, bases, attrs)
            return klass
    return Protect

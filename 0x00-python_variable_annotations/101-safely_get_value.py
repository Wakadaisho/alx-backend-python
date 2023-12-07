#!/usr/bin/env python3
"""Safely get a value from a dictionary if it exits"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Return value if key exists, otherwise return default"""
    if key in dct:
        return dct[key]
    else:
        return default

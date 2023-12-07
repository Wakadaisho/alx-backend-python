#!/usr/bin/env python3
"""Augment the following code with the
correct duck-typed annotations,"""
from typing import Any, Union, Sequence


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Retireve the first element of a list"""
    if lst:
        return lst[0]
    else:
        return None

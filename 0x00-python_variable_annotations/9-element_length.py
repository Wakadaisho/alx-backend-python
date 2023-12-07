#!/usr/bin/env python3
"""Convert iterable elements to tuples with their length"""
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Convert iterable elements to tuples with their length"""
    return [(i, len(i)) for i in lst]

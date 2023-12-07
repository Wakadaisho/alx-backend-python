#!/usr/bin/env python3
"""Return sum of mixed list of ints and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of ints and floats."""
    return sum(mxd_lst)

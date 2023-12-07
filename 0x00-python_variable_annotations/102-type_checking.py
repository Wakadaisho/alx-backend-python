#!/usr/bin/env python3
"""Correct annotation for code of a function that
duplicate a tuple into a list factor times"""


from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Duplicates a tuple into a list factor times"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

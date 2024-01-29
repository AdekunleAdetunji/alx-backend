#!/usr/bin/env python3
"""
This module contains function index_range for pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Helper function that computes the range to be used for pagination

    Args:
        page: The page where data is to be retrieved
        page_size: The size of data to be retrieved

    Return: A tuple of the start and end index of the data to be retrieved
    """
    start = (page - 1) * page_size
    return start, start + page_size

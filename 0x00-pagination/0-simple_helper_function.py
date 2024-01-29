#!/usr/bin/env python3
"""
This module contains function index_range for pagination
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Helper function that computes the range to be used for pagination

    Args:
        page: The page where data is to be retrieved
        page_size: The size of data to be retrieved

    Return: A tuple of the start and end index of the data to be retrieved
    """
    start = (page - 1) * page_size
    return start, start + page_size

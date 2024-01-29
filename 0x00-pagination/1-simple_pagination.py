#!/usr/bin/env python3
"""
This module contains a function and a class used to implement pagination
"""
import csv
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        A function that uses the index_range function defined above to get
        the content of a page within the given index
        """
        assert type(page) == int and type(page_size) == int \
            and page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        size = len(dataset)
        if start > size or end > size:
            return []

        return dataset[start: end]

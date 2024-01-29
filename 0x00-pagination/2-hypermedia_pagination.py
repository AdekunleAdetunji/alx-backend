import csv
import math
from typing import List
"""
This module contains a function and a class used to implement pagination
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Method to return the metadata of a paginated result/data
        """
        hyper = {"page": page}
        data = self.get_page(page, page_size)
        hyper["page_size"] = len(data)
        hyper["data"] = data
        hyper["prev_page"] = page - 1 if (page - 1) > 0 else None
        size = len(self.__dataset)
        total_page = math.floor(size/page_size)
        hyper["next_page"] = page + 1 if (page + 1) <= total_page else None
        hyper["total_page"] = total_page

        return hyper

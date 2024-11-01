#!/usr/bin/env python3
"""Index range"""
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end indexes for a given page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple containing the start index and end index
        for the given page.
    """
    return ((page - 1) * page_size, page * page_size)


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
        """Get page from dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        self.dataset()
        start, end = index_range(page, page_size)
        return self.__dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Get page with hypermedia pagination
        """
        data = self.get_page(page, page_size)
        total_pages = len(self.__dataset) // page_size
        if len(self.__dataset) % page_size:
            total_pages += 1
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page + 1 <= total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }

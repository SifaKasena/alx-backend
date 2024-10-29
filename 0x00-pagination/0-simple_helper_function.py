#!/usr/bin/env python3
"""Index range"""


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

#!/usr/bin/env python3
"""Hypermedia pagination
"""
import math
from typing import Tuple, List, Dict

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Returns a range of indexes of a pagination param
    '''
    first = (page - 1) * page_size
    last = first + page_size
    return (first, last)

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
            self.__dataset = dataset[1:]  # skip the header row

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''get data based on ranges of index
        '''
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        first, last = index_range(page, page_size)
        data = self.dataset()
        if first >= len(data):
            return []
        return data[first:last]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''get pagination info
        '''
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        # Determine the next and previous pages
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),  # actual size of data returned
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }


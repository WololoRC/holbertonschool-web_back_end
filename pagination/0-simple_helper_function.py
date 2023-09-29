#!/usr/bin/python3
""" simple helper function """

def index_range(page, page_size):
    """ Return a tuple of size two.
        First value: Number of page.
        Second value: Size of page.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size + 1 - 1

    return (start_index, end_index)

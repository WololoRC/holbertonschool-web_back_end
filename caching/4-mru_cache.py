#!/usr/bin/python3
""" MRU is amazing! """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ a class MRUCache that inherits from BaseCaching
        and is a caching system.
    """
    def __init__(self):
        super().__init__()
        self.mru_order = []

    def put(self, key, item):
        """ Put new elements at the begining of self.cache_data.
            If self.cache_Data >= MAS_ITEMS, pop the first item.
        """
        if item and key:
            if len(self.cache_data) >= self.MAX_ITEMS:
                rm = self.cache_data.pop(self.mru_order[0])
                print(f"DISCARD: {self.mru_order[0]}")
                self.mru_order.pop(0)
            self.cache_data.update({key: item})
            self.mru_order.insert(0, key)

    def get(self, key):
        """ Get a specific item od self.cache_Data and move it to
            the begining.
        """
        if key in self.cache_data:
            self.mru_order.insert(0, key)
            return self.cache_data.get(key)

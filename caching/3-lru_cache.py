#!/usr/bin/pyhton3
""" LRU caching is amazing! """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ a class LRUCache that inherits from BaseCaching and is a caching system """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Put new items in cahce, if len(self.cache_Data) >= MAX_ITEMS discard 
            the first item on self.cache_data.
         """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                rm = self.cache_data.popitem(last=False)
                print(f"DISCARD: {rm[0]}")
            self.cache_data.update({key: item})
    
    def get(self, key):
        """ Get a specific item of self.cache_data and put it on the end  
            of self.cache_data dict.
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)

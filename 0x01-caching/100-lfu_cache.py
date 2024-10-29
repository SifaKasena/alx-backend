#!/usr/bin/env python3
""" LFU Caching """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ LFU cache class """
    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue = []
        self.frequency = {}

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                lfu_key = min(self.frequency, key=self.frequency.get)
                self.queue.remove(lfu_key)
                del self.frequency[lfu_key]
                del self.cache_data[lfu_key]
                print("DISCARD: {}".format(lfu_key))

            if key in self.frequency:
                self.frequency[key] += 1
            else:
                self.frequency[key] = 1
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """ Get an item by key """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None

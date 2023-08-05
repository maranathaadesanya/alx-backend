#!/usr/bin/env python3
"""FIFOCache Module"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """
    FIFOCache class that inherits from BaseCaching and implements a caching system
    using the FIFO (First-In-First-Out) algorithm.
    """

    def __init__(self):
        """
        Initialize the FIFOCache instance.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache using the FIFO algorithm.

        Args:
            key: The key to be added.
            item: The item to be added.

        Returns:
            None
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Find the first item (FIFO) and remove it
            first_item_key = next(iter(self.cache_data))
            self.cache_data.pop(first_item_key)
            print(f"DISCARD: {first_item_key}")

        # Add the new key-value pair
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the value associated with the given key from the cache.

        Args:
            key: The key whose value is to be retrieved.

        Returns:
            The value associated with the key, or None if key is None
            or not present in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

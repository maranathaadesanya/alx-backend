from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
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
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]

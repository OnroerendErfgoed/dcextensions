from dogpile.cache.api import CacheBackend, NO_VALUE
from collections import OrderedDict


class LimitedSizeMemoryBackend(CacheBackend):
    """A backend that uses an ordered dictionary.
    """

    def __init__(self, arguments):
        self._cache = arguments.pop("cache_dict", OrderedDict())
        if not isinstance(self._cache, OrderedDict):
            raise ValueError("cache_dict must be instance of OrderedDict")
        self._size = arguments.pop("cache_size", 100)

    def get(self, key):
        value = self._cache.get(key, NO_VALUE)
        return value

    def get_multi(self, keys):
        ret = [self._cache.get(key, NO_VALUE) for key in keys]
        return ret

    def set(self, key, value):
        if len(self._cache) >= self._size:
            self._cache.popitem(last=False)
        self._cache[key] = value

    def set_multi(self, mapping):
        for key, value in mapping.items():
            if len(self._cache) >= self._size:
                self._cache.popitem(last=False)
            self._cache[key] = value

    def delete(self, key):
        self._cache.pop(key, None)

    def delete_multi(self, keys):
        for key in keys:
            self._cache.pop(key, None)

    def size(self):
        return len(self._cache)

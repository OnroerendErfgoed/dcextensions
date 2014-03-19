import unittest
from dcextensions.backends.memory import LimitedSizeMemoryBackend
from dogpile.cache.api import NO_VALUE


class TestMemory(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_regular_dict(self):
        my_dict = {}
        with self.assertRaises(ValueError) as cm:
            LimitedSizeMemoryBackend(arguments={"cache_dict": my_dict})
        self.assertEquals(cm.exception.args[0],
                          "cache_dict must be instance of OrderedDict")

    def test_empty(self):
        backend = LimitedSizeMemoryBackend(arguments={})
        self.assertEqual(backend.size(), 0)

    def test_default_size(self):
        backend = LimitedSizeMemoryBackend(arguments={})
        for x in range(0, 1000):
            backend.set(x, x)
        self.assertEqual(backend.size(), 100)

    def test_correct_order(self):
        backend = LimitedSizeMemoryBackend(arguments={"cache_size": 5})
        for x in range(1, 6):
            backend.set(x, x)
        for x in range(1, 6):
            self.assertEqual(backend.get(x), x)
        for x in range(6, 9):
            backend.set(x, x)
        for x in range(1, 4):
            self.assertEqual(backend.get(x), NO_VALUE)
        for x in range(4, 9):
            self.assertEqual(backend.get(x), x)
        backend.set_multi({11: 11, 12: 12, 13: 13})
        self.assertEqual(backend.get_multi({11, 12, 13}), [11, 12, 13])

    def test_get_set_multi(self):
        backend = LimitedSizeMemoryBackend(arguments={})
        backend.set_multi({1: 1, 2: 2, 3: 3})
        for x in range(1, 4):
            self.assertEqual(backend.get(x), x)
        self.assertEqual(backend.get_multi({1, 2, 3}), [1, 2, 3])

    def test_delete(self):
        backend = LimitedSizeMemoryBackend(arguments={})
        backend.set_multi({1: 1, 2: 2, 3: 3})
        for x in range(1, 4):
            self.assertEqual(backend.get(x), x)
        backend.delete_multi([1, 2, 3])
        for x in range(1, 4):
            self.assertEqual(backend.get(x), NO_VALUE)
        backend.set(5, 5)
        self.assertEqual(backend.get(5), 5)
        backend.delete(5)
        self.assertEqual(backend.get(5), NO_VALUE)

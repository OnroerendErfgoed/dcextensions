import unittest
from backend.memory import empty


class TestMemory(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty(self):
        self.assertEqual(empty(), "empty")

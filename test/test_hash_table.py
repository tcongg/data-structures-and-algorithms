import unittest
from hash_table import HashTable

class TestHashTable(unittest.TestCase):

    def test_add(self):
        table = HashTable(7)

        table.add(1, 1)
        self.assertEqual(table.get(1), 1)

        table.add(2, 2)
        table.add(3, 3)
        self.assertEqual(table.get(2), 2)
        self.assertEqual(table.get(3), 3)

    def test_get(self):
        table = HashTable(7)

        self.assertEqual(table.get(100), None)

        table.add(1, 1)
        self.assertEqual(table.get(1), 1)

        table.add(2, 2)
        table.add(3, 3)
        self.assertEqual(table.get(2), 2)
        self.assertEqual(table.get(3), 3)

    def test_exists(self):
        table = HashTable(7)

        self.assertFalse(table.exists(1111))

        table.add(1, 99)
        self.assertTrue(1)

    def test_remove(self):
        table = HashTable(7)

        table.add(1, 1)
        table.add(2, 2)
        table.add(3, 3)
        table.add(8, 99)
        table.add(16, 88)

        table.remove(1)
        self.assertEqual(table.get(1), None)
        table.remove(2)
        self.assertEqual(table.get(2), None)
        table.remove(3)
        self.assertEqual(table.get(3), None)
        table.remove(16)
        self.assertEqual(table.get(16), None)
        table.remove(8)
        self.assertEqual(table.get(8), None)
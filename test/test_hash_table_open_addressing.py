import unittest
from hash_table_open_addressing import HashTable

class TestHashTable(unittest.TestCase):

    def test_add(self):
        table = HashTable(5)

        table.add(1, 1)
        self.assertEqual(table.get(1), 1)

        table.add(2, 2)
        table.add(3, 3)
        self.assertEqual(table.get(2), 2)
        self.assertEqual(table.get(3), 3)

    def test_get(self):
        table = HashTable(5)

        self.assertEqual(table.get(100), None)

        table.add(1, 1)
        self.assertEqual(table.get(1), 1)

        table.add(2, 2)
        table.add(3, 3)
        self.assertEqual(table.get(2), 2)
        self.assertEqual(table.get(3), 3)

    def test_exists(self):
        table = HashTable(5)

        self.assertFalse(table.exists(8))

        table.add(1, 99)
        self.assertTrue(1)

    def test_remove(self):
        table = HashTable(5)

        table.add(1, 1)
        table.add(2, 2)
        table.add(3, 3)
        table.add(4, 4)

        table.remove(6)

        table.remove(1)
        self.assertEqual(table.get(1), None)
        table.remove(2)
        self.assertEqual(table.get(2), None)
        table.remove(3)
        self.assertEqual(table.get(3), None)
        table.remove(4)
        self.assertEqual(table.get(4), None)
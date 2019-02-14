import unittest
from dynamic_array import DynamicArray

class TestDynamicArray(unittest.TestCase):

    def test_size(self):
        array = DynamicArray()

        self.assertEqual(array.size(), 0)

        array.push(1)
        self.assertEqual(array.size(), 1)

    def test_capacity(self):
        array = DynamicArray()

        self.assertEqual(array.capacity(), 16)

        for i in range(16):
            array.push(i)
        self.assertEqual(array.capacity(), 16)

        for i in range(32):
            array.push(i)
        self.assertEqual(array.capacity(), 64)

        for i in range(32):
            array.pop()
        self.assertEqual(array.capacity(), 32)

        for i in range(8):
            array.pop()
        self.assertEqual(array.capacity(), 16)

        array.pop()
        self.assertEqual(array.capacity(), 16)

    def test_is_empty(self):
        array = DynamicArray()

        self.assertTrue(array.is_empty())

        array.push(1)
        self.assertFalse(array.is_empty())

    def test_push(self):
        array = DynamicArray()

        array.push(1)
        self.assertEqual(array.at(0), 1)

        array.push(2)
        self.assertEqual(array.at(0), 1)
        self.assertEqual(array.at(1), 2)

    def test_insert(self):
        array = DynamicArray()

        array.insert(0, 1)
        self.assertEqual(array.at(0), 1)

        array.insert(1, 2)
        self.assertEqual(array.at(0), 1)
        self.assertEqual(array.at(1), 2)

        array.insert(2, 3)
        self.assertEqual(array.at(0), 1)
        self.assertEqual(array.at(1), 2)
        self.assertEqual(array.at(2), 3)

        array.insert(1, 99)
        self.assertEqual(array.at(0), 1)
        self.assertEqual(array.at(1), 99)
        self.assertEqual(array.at(2), 2)
        self.assertEqual(array.at(3), 3)

    def test_prepend(self):
        array = DynamicArray()

        array.prepend(1)
        self.assertEqual(array.at(0), 1)

        array.prepend(2)
        self.assertEqual(array.at(0), 2)
        self.assertEqual(array.at(1), 1)

        array.prepend(3)
        self.assertEqual(array.at(0), 3)
        self.assertEqual(array.at(1), 2)
        self.assertEqual(array.at(2), 1)

    def test_pop(self):
        array = DynamicArray()

        with self.assertRaises(LookupError) as context:
            array.pop()
        self.assertTrue(
            "Can not pop in empty array" in str(context.exception))

        array.push(2)
        array.push(3)
        array.push(4)

        pop_2 = array.pop()
        self.assertEqual(pop_2, 4)

    def test_at(self):
        array = DynamicArray()

        with self.assertRaises(IndexError) as context:
            array.at(1)
        self.assertTrue("Index out of range" in str(context.exception))

        array.push(1)
        self.assertEqual(array.at(0), 1)

        array.push(2)
        self.assertEqual(array.at(0), 1)
        self.assertEqual(array.at(1), 2)

    def test_delete(self):
        array = DynamicArray()

        with self.assertRaises(IndexError) as context:
            array.delete(1)
        self.assertTrue("Index out of range" in str(context.exception))

        array.push(1)
        array.push(2)
        array.push(3)
        array.push(4)
        array.delete(0)
        self.assertEqual(array.size(), 3)
        self.assertEqual(array.at(0), 2)
        self.assertEqual(array.at(1), 3)
        self.assertEqual(array.at(2), 4)

        array.delete(2)
        self.assertEqual(array.at(0), 2)
        self.assertEqual(array.at(1), 3)


    def test_remove(self):
        array = DynamicArray()

        array.push(1)
        array.push(2)
        array.push(3)
        array.push(2)
        array.push(4)
        array.remove(2)
        self.assertEqual(array.size(), 3)
        self.assertEqual(array.at(0), 1)
        self.assertEqual(array.at(1), 3)
        self.assertEqual(array.at(2), 4)

        array.remove(5)
        self.assertEqual(array.at(0), 1)
        self.assertEqual(array.at(1), 3)
        self.assertEqual(array.at(2), 4)

    def test_find(self):
        array = DynamicArray()

        array.push(1)
        array.push(2)
        array.push(3)
        array.push(2)
        array.push(4)
        self.assertEqual(array.find(2), 1)
        self.assertEqual(array.find(5), -1)


if __name__ == '__main__':
    unittest.main()

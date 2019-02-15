from unittest import TestCase
from linked_list import LinkedList

class TestLinkedList(TestCase):

    def test_size(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.size(), 0)

        linked_list.push_back(1)
        self.assertEqual(linked_list.size(), 1)

    def test_is_empty(self):
        linked_list = LinkedList()

        self.assertTrue(linked_list.is_empty())

        linked_list.push_back(1)
        self.assertFalse(linked_list.is_empty())

    def test_value_at(self):
        linked_list = LinkedList()

        with self.assertRaises(IndexError) as context:
            linked_list.value_at(1)
        self.assertTrue("Index out of range" in str(context.exception))

        self.assertEqual(linked_list.size(), 0)

        linked_list.push_back(1)
        linked_list.push_back(2)
        linked_list.push_back(3)
        self.assertEqual(linked_list.value_at(0), 1)
        self.assertEqual(linked_list.value_at(1), 2)
        self.assertEqual(linked_list.value_at(2), 3)

    def test_push_front(self):
        linked_list = LinkedList()

        linked_list.push_front(1)
        linked_list.push_front(2)
        linked_list.push_front(3)
        self.assertEqual(linked_list.value_at(0), 3)
        self.assertEqual(linked_list.value_at(1), 2)
        self.assertEqual(linked_list.value_at(2), 1)

    def test_pop_front(self):
        linked_list = LinkedList()

        with self.assertRaises(LookupError) as context:
            linked_list.pop_front()
        self.assertTrue("Can not pop in empty linked list" in str(context.exception))

        linked_list.push_front(1)
        linked_list.push_front(2)
        linked_list.push_front(3)
        self.assertEqual(linked_list.pop_front(), 3)

    def test_push_back(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.size(), 0)

        linked_list.push_back(1)
        linked_list.push_back(2)
        linked_list.push_back(3)
        self.assertEqual(linked_list.value_at(0), 1)
        self.assertEqual(linked_list.value_at(1), 2)
        self.assertEqual(linked_list.value_at(2), 3)

    def test_pop_back(self):
        linked_list = LinkedList()

        with self.assertRaises(LookupError) as context:
            linked_list.pop_back()
        self.assertTrue("Can not pop in empty linked list" in str(context.exception))

        linked_list.push_back(1)
        linked_list.push_back(2)
        linked_list.push_back(3)
        self.assertEqual(linked_list.pop_back(), 3)

    def test_front(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.front(), None)

        linked_list.push_back(1)
        linked_list.push_back(2)
        linked_list.push_back(3)
        self.assertEqual(linked_list.front(), 1)

    def test_back(self):
        linked_list = LinkedList()

        self.assertEqual(linked_list.back(), None)

        linked_list.push_back(1)
        linked_list.push_back(2)
        linked_list.push_back(3)
        self.assertEqual(linked_list.back(), 3)

    def test_insert(self):
        linked_list = LinkedList()

        with self.assertRaises(IndexError) as context:
            linked_list.insert(1, 100)
            linked_list.insert(-1, 200)
        self.assertTrue("Index out of range" in str(context.exception))

        linked_list.push_back(1)
        linked_list.push_back(2)
        linked_list.push_back(3)

        linked_list.insert(0, 99)
        linked_list.insert(4, 88)
        linked_list.insert(2, 55)
        self.assertEqual(linked_list.value_at(0), 99)
        self.assertEqual(linked_list.value_at(1), 1)
        self.assertEqual(linked_list.value_at(2), 55)
        self.assertEqual(linked_list.value_at(3), 2)
        self.assertEqual(linked_list.value_at(4), 3)
        self.assertEqual(linked_list.value_at(5), 88)

    def test_erase(self):
        linked_list = LinkedList()

        with self.assertRaises(IndexError) as context:
            linked_list.erase(1)
            linked_list.erase(-1)
        self.assertTrue("Index out of range" in str(context.exception))

        linked_list.push_back(1)
        linked_list.push_back(2)
        linked_list.push_back(3)
        linked_list.push_back(4)
        linked_list.push_back(5)

        linked_list.erase(0)
        linked_list.erase(3)
        linked_list.erase(1)
        self.assertEqual(linked_list.value_at(0), 2)
        self.assertEqual(linked_list.value_at(1), 4)

    def test_value_n_from_end(self):
        linked_list = LinkedList()

        with self.assertRaises(IndexError) as context:
            linked_list.value_n_from_end(1)
            linked_list.value_n_from_end(-1)
        self.assertTrue("Index of value out of range" in str(context.exception))

        linked_list.push_back(1)
        linked_list.push_back(2)
        linked_list.push_back(3)
        linked_list.push_back(4)

        self.assertEqual(linked_list.value_n_from_end(0), 4)
        self.assertEqual(linked_list.value_n_from_end(2), 2)
        self.assertEqual(linked_list.value_n_from_end(3), 1)

    def test_reverse(self):
        linked_list = LinkedList()

        linked_list.push_back(1)
        linked_list.push_back(2)
        linked_list.push_back(3)
        linked_list.push_back(4)
        self.assertEqual(linked_list.value_at(0), 1)
        self.assertEqual(linked_list.value_at(1), 2)
        self.assertEqual(linked_list.value_at(2), 3)
        self.assertEqual(linked_list.value_at(3), 4)

        linked_list.reverse()
        self.assertEqual(linked_list.value_at(0), 4)
        self.assertEqual(linked_list.value_at(1), 3)
        self.assertEqual(linked_list.value_at(2), 2)
        self.assertEqual(linked_list.value_at(3), 1)

    def test_remove_value(self):
        linked_list = LinkedList()

        linked_list.push_back(1)
        linked_list.push_back(2)
        linked_list.push_back(3)
        linked_list.push_back(4)

        linked_list.remove_value(1)
        self.assertEqual(linked_list.value_at(0), 2)
        self.assertEqual(linked_list.value_at(1), 3)
        self.assertEqual(linked_list.value_at(2), 4)
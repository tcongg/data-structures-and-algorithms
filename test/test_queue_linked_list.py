from unittest import TestCase
from queue_linked_list import Queue

class TestQueue(TestCase):

    def test_is_empty(self):
        linked_list = Queue()

        self.assertTrue(linked_list.is_empty())

        linked_list.enqueue(1)
        self.assertFalse(linked_list.is_empty())

    def test_enqueue(self):
        linked_list = Queue()

        linked_list.enqueue(1)
        self.assertEqual(linked_list.dequeue(), 1)

        linked_list.enqueue(2)
        linked_list.enqueue(1)
        self.assertEqual(linked_list.dequeue(), 2)
        self.assertEqual(linked_list.dequeue(), 1)

        linked_list.enqueue(3)
        linked_list.enqueue(2)
        linked_list.enqueue(1)
        self.assertEqual(linked_list.dequeue(), 3)
        self.assertEqual(linked_list.dequeue(), 2)
        self.assertEqual(linked_list.dequeue(), 1)

    def test_dequeue(self):
        linked_list = Queue()

        with self.assertRaises(LookupError) as context:
            linked_list.dequeue()

        self.assertTrue("Dequeue in empty queue" in str(context.exception))

        linked_list.enqueue(1)
        self.assertEqual(linked_list.dequeue(), 1)

        linked_list.enqueue(2)
        linked_list.enqueue(1)
        self.assertEqual(linked_list.dequeue(), 2)
        self.assertEqual(linked_list.dequeue(), 1)

        linked_list.enqueue(3)
        linked_list.enqueue(2)
        linked_list.enqueue(1)
        self.assertEqual(linked_list.dequeue(), 3)
        self.assertEqual(linked_list.dequeue(), 2)
        self.assertEqual(linked_list.dequeue(), 1)
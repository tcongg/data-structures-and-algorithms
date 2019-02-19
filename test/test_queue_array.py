from unittest import TestCase
from queue_array import Queue

class TestQueue(TestCase):

    def test_is_empty(self):
        array = Queue(5)

        self.assertTrue(array.is_empty())

        array.enqueue(1)
        self.assertFalse(array.is_empty())

    def test_is_full(self):
        array = Queue(4)

        array.enqueue(1)
        self.assertEqual(array.dequeue(), 1)

        array.enqueue(2)
        array.enqueue(1)
        self.assertEqual(array.dequeue(), 2)
        self.assertEqual(array.dequeue(), 1)

        array.enqueue(3)
        array.enqueue(2)
        array.enqueue(1)
        self.assertEqual(array.dequeue(), 3)
        self.assertEqual(array.dequeue(), 2)
        self.assertEqual(array.dequeue(), 1)

        array.enqueue(4)
        array.enqueue(3)
        array.enqueue(2)
        array.enqueue(1)
        self.assertEqual(array.dequeue(), 4)
        self.assertEqual(array.dequeue(), 3)
        self.assertEqual(array.dequeue(), 2)


    def test_enqueue(self):
        array = Queue(5)

        array.enqueue(1)
        self.assertEqual(array.dequeue(), 1)

        array.enqueue(2)
        array.enqueue(1)
        self.assertEqual(array.dequeue(), 2)
        self.assertEqual(array.dequeue(), 1)

        array.enqueue(3)
        array.enqueue(2)
        array.enqueue(1)
        self.assertEqual(array.dequeue(), 3)
        self.assertEqual(array.dequeue(), 2)
        self.assertEqual(array.dequeue(), 1)

        array.enqueue(4)
        array.enqueue(3)
        array.enqueue(2)
        array.enqueue(1)
        self.assertEqual(array.dequeue(), 4)
        self.assertEqual(array.dequeue(), 3)
        self.assertEqual(array.dequeue(), 2)
        self.assertEqual(array.dequeue(), 1)

        array.enqueue(5)
        array.enqueue(4)
        array.enqueue(3)
        array.enqueue(2)
        array.enqueue(1)
        self.assertEqual(array.dequeue(), 5)
        self.assertEqual(array.dequeue(), 4)
        self.assertEqual(array.dequeue(), 3)
        self.assertEqual(array.dequeue(), 2)

    def test_dequeue(self):
        array = Queue(5)

        with self.assertRaises(LookupError) as context:
            array.dequeue()

        self.assertTrue("Queue is empty" in str(context.exception))

        array.enqueue(1)
        self.assertEqual(array.dequeue(), 1)

        array.enqueue(2)
        array.enqueue(1)
        self.assertEqual(array.dequeue(), 2)
        self.assertEqual(array.dequeue(), 1)

        array.enqueue(3)
        array.enqueue(2)
        array.enqueue(1)
        self.assertEqual(array.dequeue(), 3)
        self.assertEqual(array.dequeue(), 2)
        self.assertEqual(array.dequeue(), 1)

        array.enqueue(4)
        array.enqueue(3)
        array.enqueue(2)
        array.enqueue(1)
        self.assertEqual(array.dequeue(), 4)
        self.assertEqual(array.dequeue(), 3)
        self.assertEqual(array.dequeue(), 2)
        self.assertEqual(array.dequeue(), 1)

        array.enqueue(5)
        array.enqueue(4)
        array.enqueue(3)
        array.enqueue(2)
        array.enqueue(1)
        self.assertEqual(array.dequeue(), 5)
        self.assertEqual(array.dequeue(), 4)
        self.assertEqual(array.dequeue(), 3)
        self.assertEqual(array.dequeue(), 2)
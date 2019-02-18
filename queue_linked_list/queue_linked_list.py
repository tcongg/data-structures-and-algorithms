class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self._head = None
        self._tail = None

    def is_empty(self):
        """
        Checks list is empty or not
        Time Complexity: O(1)
        """
        return self._head is self._tail is None

    def enqueue(self, value):
        """
        Adds value at position at tail
        Time Complexity: O(1)
        """
        if self._tail is None:
            self._tail = self._head = Node(value)
        else:
            self._tail.next = Node(value)
            self._tail = self._tail.next

    def dequeue(self):
        """
        Returns value and removes least recently added element
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise LookupError("Dequeue in empty queue")

        dequeue_value = self._head.data

        if self._head == self._tail:
            self._tail = self._head = None
        else:
            self._head = self._head.next

        return dequeue_value
class Queue:

    def __init__(self, capacity):
        self._capacity = capacity
        self._items = [None] * (self._capacity + 1)
        self._head = 0
        self._tail = 0

    def capacity(self):
        """
        Returns max number of items array can hold
        Time complexity: O(1)
        """
        return self._capacity

    def is_empty(self):
        """
        Checks array is empty or not
        Time complexity: O(1)
        """
        return self._head == self._tail

    def is_full(self):
        """
        Checks array is full or not
        Time complexity: O(1)
        """
        return self._head == (self._tail + 1) % (self._capacity + 1)

    def enqueue(self, value):
        """
        Adds item at end of available storage
        Time complexity: O(1)
        """
        if self.is_full():
            return

        self._items[self._tail] = value
        self._tail = (self._tail + 1) % (self._capacity + 1)

    def dequeue(self):
        """
        Returns value and removes least recently added element
        Time complexity: O(1)
        """
        if self.is_empty():
            raise LookupError("Queue is empty")

        dequeue_value = self._items[self._head]
        self._items[self._head] = None
        self._head = (self._head + 1) % (self._capacity + 1)
        return dequeue_value
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self._head = None
        self._size = 0

    def size(self):
        """
        Returns number of data elements in list
        Time Complexity: O(1)
        """
        return self._size

    def is_empty(self):
        """
        Returns true if empty
        Time Complexity: O(1)
        """
        return self._size == 0

    def value_at(self, index):
        """
        Returns the value of the nth item (starting at 0 for first)
        Time Complexity: O(n)
        """
        if index >= self._size or index < 0:
            raise IndexError("Index out of range")

        value = self._head

        for i in range(self._size):
            if i == index:
                return value.data
            value = value.next
        
        return value

    def push_front(self, value):
        """
        Adds an item to the front of the list
        Time Complexity: O(1)
        """
        head_value = self._head
        self._head = Node(value)
        self._head.next = head_value
        self._size += 1

    def pop_front(self):
        """
        Remove front item and return its value
        Time Complexity: O(1)
        """
        if self._size == 0:
            raise LookupError("Can not pop in empty linked list")

        pop_value = self._head.data
        self._head = self._head.next
        self._size -= 1
        return pop_value

    def push_back(self, value):
        """
        Adds an item to the end of the list
        Time Complexity: O(n)
        """
        if self._head is None:
            self._head = Node(value)
        else:
            last_node = self._head
            for i in range(self._size - 1):
                last_node = last_node.next
            last_node.next = Node(value)

        self._size += 1

    def pop_back(self):
        """
        Remove end item and return its value
        Time Complexity: O(n)
        """
        if self._size == 0:
            raise LookupError("Can not pop in empty linked list")

        if self._size == 1:
            pop_value = self._head.data
            self._head = None
        else:
            value = self._head
            for i in range(self._size - 2):
                value = value.next
            pop_value = value.next.data

        self._size -= 1
        return pop_value

    def front(self):
        """
        Get value of front item
        Time Complexity: O(1)
        """
        if self.is_empty():
            return None

        return self._head.data

    def back(self):
        """
        Get value of end item
        Time Complexity: O(n)
        """
        if self.is_empty():
            return None

        return self.value_at(self._size - 1)

    def insert(self, index, value):
        """
        Insert value at index, so current item at that index is pointed to by new item at index
        Time Complexity: O(n)
        """
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")

        node_value = value

        if index == 0:
            head_value = self._head
            self._head = Node(value)
            self._head.next = head_value
        else:
            value = self._head
            for i in range(0, index - 1):
                value = value.next

            new_node = Node(node_value)
            new_node.next = value.next
            value.next = new_node

        self._size += 1

    def erase(self, index):
        """
        Removes node at given index
        Time Complexity: O(n)
        """
        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")

        if index == 0:
            self._head = self._head.next
        else:
            value = self._head
            for i in range(0, index - 1):
                value = value.next
            value.next = value.next.next

        self._size -= 1

    def value_n_from_end(self, n):
        """
        Returns the value of the node at nth position from the end of the list
        Time Complexity: O(n)
        """
        if n < 0 or n >= self._size:
            raise IndexError("Index of value out of range")

        value = self._head
        for i in range(0, self._size - 1 - n):
            value = value.next
        return value.data

    def reverse(self):
        """
        Reverse the list
        Time Complexity: O(n)
        """
        value = self._head
        prev_node = None

        for i in range(self._size):
            next_node = value.next
            value.next = prev_node
            prev_node = value
            value = next_node
        self._head = prev_node

    def remove_value(self, value):
        """
        Removes the first item in the list with this value
        Time Complexity: O(n)
        """
        if self.is_empty():
            return

        head_value = self._head
        tmp = None

        if head_value is not None:
            if head_value.data == value:
                self._head = head_value.next
        else:
            for i in range(self._size):
                if head_value.data == value:
                    break
                tmp = _head_value
                head_value = head_value.next

            if head_value is None:
                return

            tmp.next = head_value.next

        self._size -= 1
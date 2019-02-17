class Node:

    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node

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

        moved_node = self._head

        for i in range(self._size):
            if i == index:
                return moved_node.data
            moved_node = moved_node.next

    def push_front(self, value):
        """
        Adds an item to the front of the list
        Time Complexity: O(1)
        """
        self._head = Node(value, self._head)
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
            moved_node = self._head
            for i in range(self._size - 2):
                moved_node = moved_node.next
            pop_value = moved_node.next.data

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

        if index == 0:
            self._head = Node(value, self._head)
        else:
            moved_node = self._head
            for i in range(0, index - 1):
                moved_node = moved_node.next

            moved_node.next = Node(value, moved_node.next)

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
            moved_node = self._head

            for i in range(0, index - 1):
                moved_node = moved_node.next
            moved_node.next = moved_node.next.next

        self._size -= 1

    def value_n_from_end(self, n):
        """
        Returns the value of the node at nth position from the end of the list
        Time Complexity: O(n)
        """
        if n < 0 or n >= self._size:
            raise IndexError("Index of value out of range")

        return self.value_at(self._size - n - 1)

    def reverse(self):
        """
        Reverse the list
        Time Complexity: O(n)
        """
        temp_node = self._head
        prev_node = None

        for i in range(self._size):
            next_node = temp_node.next
            temp_node.next = prev_node
            prev_node = temp_node
            temp_node = next_node
        self._head = prev_node

    def remove_value(self, value):
        """
        Removes the first item in the list with this value
        Time Complexity: O(n)
        """
        if self.is_empty():
            return

        moved_node = self._head

        if self._head == value:
            self._head = self._head.next
            self._size -= 1
        else:
            while moved_node.next is not None:
                if moved_node.next.data == value:
                    moved_node.next = moved_node.next.next
                    break
                else:
                    moved_node = moved_node.next              
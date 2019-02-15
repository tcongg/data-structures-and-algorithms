class DynamicArray:
    def __init__(self):
        self._size = 0
        self._capacity = 16
        self._items = [None] * self._capacity

    def size(self):
        """
        Return number of items stored in DynamicArray
        Time complexity: O(1)
        """
        return self._size

    def capacity(self):
        """
        Return number of items DynamicArray can hold
        Time complexity: O(1)
        """
        return self._capacity

    def is_empty(self):
        """
        Check DynamicArray is empty or not. Return True if empty, False if not
        Time complexity: O(1)
        """
        return self._size == 0

    def push(self, item):
        """
        Add given item to end of DynamicArray
        Time complexity: O(1)
        """
        self.insert(self._size, item)

    def insert(self, index, item):
        """
        Inserts item at index
        Time complexity: O(n)
        """
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")

        self.__resize()
        for i in range(self._size, index, -1):
            self._items[i] = self._items[i - 1]
        self._items[index] = item
        self._size += 1

    def prepend(self, item):
        """
        Insert given item at index 0
        Time complexity: O(n)
        """
        self.insert(0, item)

    def pop(self):
        """
        Remove last item and return its value
        Time complexity: O(1)
        """
        if self._size == 0:
            raise LookupError("Can not pop in empty array")

        pop_value = self._items[self._size - 1]
        self.delete(self._size - 1)
        return pop_value

    def at(self, index):
        """
        Returns item at given index, blows up if index out of bounds
        Time complexity: O(1)
        """
        if index >= self._size or index < 0:
            raise IndexError("Index out of range")
        else:
            return self._items[index]

    def delete(self, index):
        """
        Delete item at index, shifting all trailing elements left
        Time complexity: O(n)
        """
        if index >= self._size or index < 0:
            raise IndexError("Index out of range")

        for i in range(index, self._size - 1):
            self._items[i] = self._items[i + 1]
        self._size -= 1
        self.__resize()

    def remove(self, item):
        """
        Remove all items with given value
        Time complexity: O(n^2)
        """
        moved_count = 0
        
        for i in self._items:
            if i != item:
                self._items[moved_count] = i
                moved_count += 1

        self._size = moved_count
        self.__resize()

    def find(self, item):
        """
        Looks for value and returns first index with that value, -1 if not found
        Time complexity: O(n)
        """
        for i in range(self._size):
            if self._items[i] == item:
                return i
        return -1

    def __resize(self):
        """
        When you reach capacity, resize to double the size
        When popping an item, if size is 1/4 of capacity, resize to half
        Time complexity: O(n)
        """
        if self._size == self._capacity:
            new_capacity = self._capacity * 2
        elif self._size > 0 and self._size <= self._capacity / 4 and self._capacity > 16 :
            new_capacity = self._capacity // 2
        else:
            return

        new_arr = [None] * new_capacity

        for i in range(self._size):
            new_arr[i] = self._items[i]
        del self._items[:]

        self._items = new_arr
        self._capacity = new_capacity

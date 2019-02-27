class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:

    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity
        self._table = [None] * self._capacity

    def hash_function(self, key):
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)

        return hash % self._capacity

    def add(self, key, value):
        index = self.hash_function(str(key))

        new_value = self._table[index]

        if new_value is None:
            self._table[index] = Node(key, value)
            return

        tmp = new_value
        while new_value is not None:
            tmp = new_value
            new_value = new_value.next
        tmp.next = Node(key, value)

    def get_key(self, key):
        index = self.hash_function(str(key))
        return

    def is_exist(self, key):
        index = self.hash_function(str(key))
        new_value = self._table[index]

        if new_value is None:
            return False
        
        return True

    def remove(self, key):
        index = self.hash_function(str(key))
        return

table = HashTable(7)
table.add(8, 1999)
table.add(8, 1900)
print(table.is_exist(8))
print(table.is_exist(1111))
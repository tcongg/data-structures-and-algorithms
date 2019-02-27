class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self._head = None
        self._size = 0

    def push_back(self, key, value):
        if self._head is None:
            self._head = Node(key, value)
        else:
            last_node = self._head

            for i in range(self._size - 1):
                last_node = last_node.next
            last_node.next = Node(key, value)

        self._size += 1  

class HashTable:

    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity
        self._table = [LinkedList()] * self._capacity

    def hash_function(self, key):
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)

        return hash % self._capacity

    def add(self, key, value):
        table_index = self.hash_function(str(key))
        new_node = Node(key, value)

        self._table[table_index] = value

    def get_key(self, key):
        table_index = self.hash_function(str(key))
        return

    def is_exist(self, key):
        table_index = self.hash_function(str(key))
        return

    def remove(self, key):
        table_index = self.hash_function(str(key))
        return

    def display(self):
        for i in self._table:
            print(i)

table = HashTable(7)
table.add(111, 1999)
table.display()
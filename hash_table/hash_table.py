class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:

    def __init__(self, capacity):
<<<<<<< HEAD
        self._capacity = capacity
        self._table = [None] * self._capacity

    def __hash(self, key):
=======
        self._size = 0
        self._capacity = capacity
        self._table = [None] * self._capacity

    def hash(self, key):
>>>>>>> 43e0b60e9c071000911bd62be8d18b279b5a7556
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)

        return hash % self._capacity

    def add(self, key, value):
<<<<<<< HEAD
        node = self._table[self.__hash(str(key))]

        if not node:
            self._table[self.__hash(str(key))] = Node(key, value)
=======
        index = self.hash(str(key))

        node = self._table[index]

        if node is None:
            self._table[index] = Node(key, value)
>>>>>>> 43e0b60e9c071000911bd62be8d18b279b5a7556
            return

        while node.next:
            node = node.next
        node.next = Node(key, value)


    def get(self, key):
<<<<<<< HEAD
        node = self._table[self.__hash(str(key))]
=======
        index = self.hash(str(key))
        node = self._table[index]
>>>>>>> 43e0b60e9c071000911bd62be8d18b279b5a7556

        while node:
            if node.key == key:
                return node.value

            node = node.next

        return None

    def exists(self, key):
<<<<<<< HEAD
        node = self._table[self.__hash(str(key))]
=======
        index = self.hash(str(key))
        node = self._table[index]
>>>>>>> 43e0b60e9c071000911bd62be8d18b279b5a7556

        while node:
            if node.key == key:
                return True
            
            node = node.next

<<<<<<< HEAD
        return False

    def remove(self, key):
        node = self._table[self.__hash(str(key))]

        while node is not None:
            if node is None:
                return
            elif node.key == key:
                self._table[self.__hash(str(key))] = node.next
            else:
                if node.key == key:
=======
        if not node:
            return False

    def remove(self, key):
        index = self.hash(str(key))
        node = self._table[index]

        while node:
            if node is None:
                return None
            elif node.key == key:
                self._table[index] = node.next
            else:
                if node.next.key == key:
>>>>>>> 43e0b60e9c071000911bd62be8d18b279b5a7556
                    node.next = node.next.next
                    break
            node = node.next
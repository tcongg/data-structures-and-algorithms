class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:

    def __init__(self, capacity):
        self._capacity = capacity
        self._table = [None] * self._capacity

    def __hash(self, key):
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)

        return hash % self._capacity

    def add(self, key, value):
        node = self._table[self.__hash(str(key))]

        if not node:
            self._table[self.__hash(str(key))] = Node(key, value)
            return

        while node.next:
            node = node.next
        node.next = Node(key, value)


    def get(self, key):
        node = self._table[self.__hash(str(key))]

        while node:
            if node.key == key:
                return node.value

            node = node.next

        return None

    def exists(self, key):
        node = self._table[self.__hash(str(key))]

        while node:
            if node.key == key:
                return True
            
            node = node.next

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
                    node.next = node.next.next
                    break
            node = node.next
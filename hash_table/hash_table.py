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

    def hash(self, key):
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)

        return hash % self._capacity

    def add(self, key, value):
        index = self.hash(str(key))

        node = self._table[index]

        if node is None:
            self._table[index] = Node(key, value)
            return

        while node.next:
            node = node.next
        node.next = Node(key, value)


    def get(self, key):
        index = self.hash(str(key))
        node = self._table[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next

    def exists(self, key):
        index = self.hash(str(key))
        node = self._table[index]

        if node is None:
            return False

        if node.key == key:
            return True

        while node:
            node = node.next
            if node.key == key:
                return True

            return False

    def remove(self, key):
        index = self.hash(str(key))
        remove_value = self._table[index]

        if not remove_value:
            return

        if remove_value.key == key:
            remove_value = remove_value.next
        else:
            move = remove_value

            while move is not None:
                if move.next.key == key:
                    move.next = move.next.next
                    break

                move = move.next

            if move.next is None:
                return
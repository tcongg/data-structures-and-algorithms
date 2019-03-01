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
        new_value = self._table[index]

        while new_value is not None:
            if new_value.key == key:
                print(new_value.value)
            new_value = new_value.next

    def is_exist(self, key):
        index = self.hash_function(str(key))
        new_value = self._table[index]

        if new_value is None:
            return False

        if new_value.key == key:
            return True

        while new_value is not None:
            new_value = new_value.next
            if new_value.key == key:
                return True

            return False

    def remove(self, key):
        index = self.hash_function(str(key))
        remove_value = self._table[index]

        if remove_value is None:
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
class Value():

    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable():

    def __init__(self, capacity):
        self._size = 0
        self._capacity = capacity
        self._table = [None] * self._capacity

    def __hash(self, key, i):
        hash = 5381
        for x in key:
            hash = ((hash << 5) + hash) + ord(x)

        return (hash + i) % self._capacity

    def add(self, key, value):
        self.__resize()

        for i in range(self._capacity):
            index = self.__hash(str(key), i)
            if self._table[index] is None:
                self._table[index] = Value(key, value)
                self._size += 1
                return

    def get(self, key):
        index = self.__hash(str(key), 0)

        if self.exists(key):
            return self._table[index].value

        return None

    def exists(self, key):     
        index = self.__hash(str(key), 0)
        if self._table[index] == None:
            return False

        if self._table[index].key == key:
            return True

        return False

    def remove(self, key):
        index = self.__hash(str(key), 0)

        if self.exists(key) is False:
            return
        
        self._table[index] = Value(None, None)

    def __resize(self):
        if self._size == self._capacity:
            new_capacity = self._capacity * 2
        else:
            return

        new_table = [None] * new_capacity

        for i in range(self._capacity):
            new_table[i] = self._table[i]

        del self._table[:]

        self._table = new_table
        self._capacity = new_capacity
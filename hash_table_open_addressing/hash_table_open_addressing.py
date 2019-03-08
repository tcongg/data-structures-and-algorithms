class Value():

    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable():

    def __init__(self):
        self._size = 0
        self._capacity = 4
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
            if self._table[index] is None or self._table[index].value is "Flag":
                self._table[index] = Value(key, value)
                self._size += 1
                return

    def get(self, key):
        for i in range(self._capacity):
            index = self.__hash(str(key), i)

            if self._table[index] is not None and self._table[index].key == key:
                return self._table[index].value

        return None

    def exists(self, key):     
        for i in range(self._capacity):
            index = self.__hash(str(key), i)
            if self._table[index] == None:
                return False

            if self._table[index].key == key:
                return True

        return False

    def remove(self, key):
        for i in range(self._capacity):
            index = self.__hash(str(key), i)
            if self._table[index] != None and self._table[index].key == key:
                self._table[index] = Value(None, "Flag")
                self._size -= 1
                self.__resize()
                return

    def __resize(self):
        if self._size == self._capacity:
            new_capacity = self._capacity * 2
        elif self._size > 0 and self._size <= self._capacity / 4 and self._capacity > 4:
            new_capacity = self._capacity // 2
        else:
            return
        
        self._capacity = new_capacity
        new_table = [None] * self._capacity

        for item in self._table:
            if item is not None and item.value != "Flag":
                for i in range(self._capacity):
                    new_index = self.__hash(str(item.key), i)
                    if new_table[new_index] is None:
                        new_table[new_index] = item
                        break

        del self._table[:]

        self._table = new_table
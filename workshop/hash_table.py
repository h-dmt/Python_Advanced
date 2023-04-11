"""
A class HashTable which implements the functionality of a customised dictionary
which dynamically allocates memory
"""


class HashTable:
    def __init__(self):
        self.__size = 4
        self.__keys = [None] * self.__size
        self.__values = [None] * self.__size

    def __setitem__(self, key, value):
        index = self.__calculate_index(key)
        self.__keys[index] = key
        self.__values[index] = value

    def __getitem__(self, key, default=None):
        try:
            index = self.__keys.index(key)
        except IndexError:
            return default

        val = self.__values[index]
        return val

    def __calculate_index(self, key):
        index = sum(ord(k) for k in key) % self.__size
        index = self.__set_index(index)

        return index

    def __set_index(self, idx: int):
        if self.__keys[idx] is not None:
            if len(self) == self.__size:
                self.__extend()
            return self.__set_index(idx + 1)

        return idx

    def __extend(self):
        self.__keys = self.__keys + [None] * self.__size
        self.__values = self.__values + [None] * self.__size
        self.__size *= 2

    def add(self, key, value):
        # using the __setitem__ method
        self[key] = key

    def get(self, key, default=None):
        try:
            index = self.__keys.index(key)
        except IndexError:
            return default

        return self.__values[index]

    def insert(self, key, value):
        idx = self.__calculate_index(key)
        self.__keys[idx] = key
        self.__values[idx] = value

    def remove(self, key):
        try:
            index = self.__keys.index(key)
        except KeyError:
            raise ValueError(f"{key} not found")

        self.__keys[index] = None
        self.__values[index] = None

    def remove_all(self):
        for i in range(len(self)):
            if self.__keys[i] is not None:
                self.__keys[i] = None
                self.__values[i] = None
        self.__size = 4
        self.__keys = [None] * self.__size
        self.__values = [None] * self.__size

    def __len__(self):
        return len([k for k in self.__keys if k is not None])

    def __str__(self):
        result = ["{"]
        for i in range(len(self)):
            if self.__keys[i] is not None:
                result.append(str(self.__keys[i]) + ": " + str(self.__values[i]))
                result.append(", ")
        result += ['}']

        return "".join(result)

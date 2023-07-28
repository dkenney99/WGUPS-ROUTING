class HashTable:
    def __init__(self):
        self.size = 41  # Prime numbers are less likely to have hash collisions.
        self.table = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def insert(self, key, item):
        hash_index = self._hash(key)
        if not self.table[hash_index]:
            self.table[hash_index] = [(key, item)]
        else:
            for pair in self.table[hash_index]:
                if pair[0] == key:
                    pair[1] = item  # If key already exists, update value
                    break
            else:
                self.table[hash_index].append((key, item))  # If key not found, append new pair

    def lookup(self, key):
        hash_index = self._hash(key)
        if self.table[hash_index] is not None:
            for pair in self.table[hash_index]:
                if pair[0] == key:
                    return pair[1]  # Return the Package object if key found
        return None  # Return None if key not found

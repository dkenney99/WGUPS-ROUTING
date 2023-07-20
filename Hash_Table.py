class HashTable:
    def __init__(self, capacity=40):
        self.table = [[] for _ in range(capacity)]

    def put(self, key, value):
        bucket_index = hash(key) % len(self.table)
        bucket = self.table[bucket_index]
        for index, kv_pair in enumerate(bucket):
            if kv_pair[0] == key:
                bucket[index] = (key, value)
                break
        else:
            bucket.append((key, value))

    def get(self, key):
        bucket_index = hash(key) % len(self.table)
        bucket = self.table[bucket_index]
        for kv_pair in bucket:
            if kv_pair[0] == key:
                return kv_pair[1]
        return None

    def remove(self, key):
        bucket_index = hash(key) % len(self.table)
        bucket = self.table[bucket_index]
        for index, kv_pair in enumerate(bucket):
            if kv_pair[0] == key:
                del bucket[index]
                break

    def size(self):
        return len(self.table)  # Return the number of key-value pairs in the hash table

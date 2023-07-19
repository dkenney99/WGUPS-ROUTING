class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, delivery_address, delivery_deadline, delivery_city, delivery_zip_code, package_weight):
        # Delivery status is set to 'At the hub' initially
        delivery_status = 'At the hub'

        # Delivery time is None initially
        delivery_time = None

        hash_index = self.hash_function(key)

        for pair in self.table[hash_index]:
            # If key is found, update the existing pair
            if pair[0] == key:
                pair[1][0] = delivery_address
                pair[1][1] = delivery_deadline
                pair[1][2] = delivery_city
                pair[1][3] = delivery_zip_code
                pair[1][4] = package_weight
                pair[1][5] = delivery_status
                pair[1][6] = delivery_time
                return True

        # If key not found, add new pair
        self.table[hash_index].append([key, [delivery_address, delivery_deadline, delivery_city, delivery_zip_code, package_weight, delivery_status, delivery_time]])
        return True

    def lookup(self, key):
        hash_index = self.hash_function(key)

        for pair in self.table[hash_index]:
            if pair[0] == key:
                # Return the package details
                return pair[1]
        # Return None if key not found
        return None
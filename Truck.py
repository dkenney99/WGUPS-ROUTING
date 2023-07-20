# Truck class
class Truck:

    def __init__(self, max_capacity, max_speed, current_load, packages_array, total_mileage, current_address,
                 start_time):
        self.max_capacity = max_capacity
        self.max_speed = max_speed
        self.current_load = current_load
        self.packages_array = packages_array
        self.total_mileage = total_mileage
        self.current_address = current_address
        self.start_time = start_time
        self.current_time = start_time

    def __str__(self):
        return f"{self.max_capacity}, {self.max_speed}, {self.current_load}, {self.packages_array}, {self.total_mileage}, {self.current_address}, {self.start_time}"

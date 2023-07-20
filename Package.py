# Package class
class Package:

    def __init__(self, package_id, street_address, package_city, package_state, postal_code, deadline, package_weight, delivery_status):
        self.time_of_departure = None
        self.time_of_delivery = None
        self.package_id = package_id
        self.package_city = package_city
        self.package_state = package_state
        self.postal_code = postal_code
        self.street_address = street_address
        self.deadline = deadline
        self.package_weight = package_weight
        self.delivery_status = delivery_status

    def __str__(self):
        return f"{self.package_id}, {self.street_address}, {self.package_city}, {self.package_state}, {self.postal_code}, {self.deadline}, {self.package_weight}, {self.time_of_delivery}, {self.delivery_status}"

    def __lt__(self, other):
        if isinstance(other, Package):
            return self.package_id < other.package_id
        return NotImplemented

    def adjust_delivery_status(self, compare_time):
        if self.time_of_delivery < compare_time:
            self.delivery_status = "Delivered"
        elif self.time_of_departure > compare_time:
            self.delivery_status = "En route"
        else:
            self.delivery_status = "At Hub"

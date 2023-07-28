class Truck:
    def __init__(self, id, capacity=16):
        self.id = id
        self.capacity = capacity
        self.packages = []

    def load_package(self, package):
        if len(self.packages) < self.capacity:
            self.packages.append(package)
            return True
        else:
            return False  # Truck is full

    def deliver_package(self, package):
        if package in self.packages:
            self.packages.remove(package)
            package.status = "Delivered"
            return True
        else:
            return False  # Package not in this truck

    def __str__(self):
        return f'Truck ID: {self.id}, Packages: {[package.id for package in self.packages]}'

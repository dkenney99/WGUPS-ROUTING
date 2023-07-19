from queue import PriorityQueue
from Hash_Table import HashTable
from Package import Package

import csv
import datetime
import Truck


def read_csv_file(filename):
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        return list(csv_reader)


distances_data = read_csv_file("Data/distances.csv")
addresses_data = read_csv_file("Data/address_list.csv")
packages_data = read_csv_file("Data/packages.csv")


def create_package_from_data(data):
    package_ID = int(data[0])
    package_address = data[1]
    package_city = data[2]
    package_state = data[3]
    package_zip_code = data[4]
    package_deadline = data[5]
    package_weight = data[6]
    package_status = "At Hub"

    return Package(package_ID, package_address, package_city, package_state, package_zip_code, package_deadline,
                   package_weight, package_status)


def load_package_attributes(filename, package_hash_table):
    package_data = read_csv_file(filename)
    for package in package_data:
        p = create_package_from_data(package)
        package_hash_table.insert(p.ID, p)


def get_distance_between_addresses(address1_index, address2_index):
    try:
        # Try to get the distance from the first location in the matrix
        distance = distances_data[address1_index][address2_index]
        if distance == '':
            # If the distance is not found, try to get it from the second location
            distance = distances_data[address2_index][address1_index]
            if distance == '':
                # If the distance is still not found, raise an exception
                raise ValueError(f"No distance found between addresses {address1_index} and {address2_index}")
        return float(distance)
    except IndexError:
        # This exception will be raised if address1_index or address2_index is out of the range of the distance_data
        # matrix
        print(f"Index out of range: {address1_index} or {address2_index}")
    except ValueError as e:
        # This exception will be raised if the distance cannot be converted to float or if no distance is found
        # between the addresses
        print(e)


def get_address_number(address):
    for row in addresses_data:
        if address == row[2]:
            return int(row[0])
    print(f"Address '{address}' not found in Address Data.")
    return None


def create_truck(capacity, speed, packages, start_mileage, start_address, start_time):
    return Truck.Truck(capacity, speed, None, packages, start_mileage, start_address, start_time)


def setup_package_data():
    hash_table_for_packages = HashTable()
    load_package_attributes("Data/packages.csv", hash_table_for_packages)
    return hash_table_for_packages


# Create truck objects
truck1 = create_truck(16, 18, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                      datetime.timedelta(hours=8))
truck2 = create_truck(16, 18, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
                      "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))
truck3 = create_truck(16, 18, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
                      datetime.timedelta(hours=9, minutes=5))

# Setup package data
package_hash_table = setup_package_data()

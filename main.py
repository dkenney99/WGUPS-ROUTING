# NHP3 TASK 2: WGUPS ROUTING PROGRAM IMPLEMENTATION
# DATA STRUCTURES AND ALGORITHMS II — C950
# Daniel Kenney - 006160738

# Import necessary modules
from queue import PriorityQueue
from Hash_Table import HashTable
from Package import Package

import csv
import datetime
import Truck


# Define a function to read a CSV file and return its contents as a list
def read_csv_file(filename):
    with open(filename, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        return list(csv_reader)


# Read the distances, addresses, and packages data from their respective CSV files
distances_data = read_csv_file("Data/distances.csv")
addresses_data = read_csv_file("Data/address_list.csv")
packages_data = read_csv_file("Data/packages.csv")


# Define a function to create a package instance from the given data
def create_package_from_data(data):
    # Extract details from the data
    package_ID = int(data[0])
    package_address = data[1]
    package_city = data[2]
    package_state = data[3]
    package_zip_code = data[4]
    package_deadline = data[5]
    package_weight = data[6]
    package_status = "At Hub"

    # Create and return a Package instance
    return Package(package_ID, package_address, package_city, package_state, package_zip_code, package_deadline,
                   package_weight, package_status)


# Define a function to load the package attributes from a CSV file into a hash table
def load_package_attributes(filename, package_hash_table):
    # Read the package data from the CSV file
    package_data = read_csv_file(filename)

    # For each package in the data, create a Package instance and add it to the hash table
    for package in package_data:
        p = create_package_from_data(package)
        package_hash_table.put(p.package_id, p)


# Define a function to get the distance between two addresses
def get_distance_between_addresses(address1_index, address2_index):
    try:
        # Try to get the distance from the first location in the distances_data matrix
        distance = distances_data[address1_index][address2_index]

        if distance == '':
            # If the distance is not found, try to get it from the second location
            distance = distances_data[address2_index][address1_index]
            if distance == '':
                # If the distance is still not found, raise an exception
                raise ValueError(f"No distance found between addresses {address1_index} and {address2_index}")

        # Convert the distance to a float and return it
        return float(distance)
    except IndexError:
        # Print an error message if the address indices are out of range
        print(f"Index out of range: {address1_index} or {address2_index}")
    except ValueError as e:
        # Print an error message if the distance cannot be converted to a float
        print(e)


# Define a function to get the number associated with a given address
def get_address_number(address):
    # Search for the address in the addresses_data list
    for row in addresses_data:
        if address == row[2]:
            # Return the associated number
            return int(row[0])

    # Print an error message if the address is not found
    print(f"Address '{address}' not found in Address Data.")
    return None


# Define a function to create a Truck instance
def create_truck(capacity, speed, packages, start_mileage, start_address, start_time):
    return Truck.Truck(capacity, speed, None, packages, start_mileage, start_address, start_time)


# Define a function to setup the package data
def setup_package_data():
    # Create a hash table for the packages
    hash_table_for_packages = HashTable()

    # Load the package attributes from the CSV file into the hash table
    load_package_attributes("Data/packages.csv", hash_table_for_packages)

    # Return the hash table
    return hash_table_for_packages


# Create three Truck instances
truck1 = create_truck(16, 18, [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                      datetime.timedelta(hours=8))
truck2 = create_truck(16, 18, [3, 6, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
                      "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))
truck3 = create_truck(16, 18, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
                      datetime.timedelta(hours=9, minutes=5))

# Setup the package data
package_hash_table = setup_package_data()


# Define a function to deliver the packages for a given truck
def delivering_packages(truck):
    # Create a priority queue for packages to be delivered
    not_delivered = PriorityQueue()

    for packageID in truck.packages_array:
        package = package_hash_table.get(packageID)

        # Compute the priority for the package
        distance = get_distance_between_addresses(get_address_number(truck.current_address),
                                                  get_address_number(package.street_address))
        deadline_hour = int(package.deadline.split(':')[0]) if package.deadline != 'EOD' else 24
        priority = distance + deadline_hour

        # Items in the priority queue are tuples where the first element is the priority
        not_delivered.put((priority, package))

    # Clear the package list of the truck for reordering
    truck.packages_array.clear()

    # Continually deliver the package with the highest priority (smallest number)
    while not not_delivered.empty():
        priority, next_package = not_delivered.get()

        # Compute the distance to the next package's address
        next_address = get_distance_between_addresses(get_address_number(truck.current_address),
                                                      get_address_number(next_package.street_address))

        # Update truck and package details
        truck.packages_array.append(next_package.package_id)
        truck.total_mileage += next_address
        truck.current_address = next_package.street_address
        truck.start_time += datetime.timedelta(hours=next_address / 18)
        next_package.time_of_delivery = truck.start_time
        next_package.time_of_departure = truck.current_time


# Define a function to execute the deliveries for a list of trucks
def execute_deliveries(trucks):
    # Deliver packages for each truck in order
    for i in range(len(trucks)):
        if i < len(trucks) - 1:
            # Ensure that the next truck does not leave until the current truck has finished its deliveries
            trucks[i + 1].depart_time = trucks[i].current_time
        delivering_packages(trucks[i])


# Define a function to list all packages in the hash table
def list_all_packages(package_hash_table):
    # Iterate over all package IDs in the hash table
    for packageID in range(1, package_hash_table.size() + 1):
        # Retrieve the package corresponding to the current package ID
        package = package_hash_table.get(packageID)

        # If the package exists, print its information
        if package:
            print(f"Package ID: {package.package_id}")
            print(f"Address: {package.street_address}")
            print(f"City: {package.package_city}")
            print(f"State: {package.package_state}")
            print(f"Zipcode: {package.postal_code}")
            print(f"Deadline: {package.deadline}")
            print(f"Weight: {package.package_weight}")
            print(f"Status: {package.delivery_status}")
            print(f"Delivery time: {package.time_of_delivery}")
            print("\n")
        else:
            print(f"No package found with ID {packageID}\n")


# Define a function to list all trucks in the list
def list_all_trucks(trucks):
    for truck in trucks:
        print(truck)


# Create a list of trucks
trucks = [truck1, truck2, truck3]

# Execute deliveries for all trucks
execute_deliveries(trucks)


# Main class
class WGUPSProgram:
    @staticmethod
    def start():
        # Initial messages
        print("WGUPS Routing Program Implementation by Daniel Kenney")
        print("Cumulative mileage of all trucks combined: ")
        print(truck1.total_mileage + truck2.total_mileage + truck3.total_mileage)

        # User password prompt
        user_password = input("Please enter your password (hint, the password is password) ")
        if user_password != "password":
            print("Password incorrect. Exiting...")
            return

        try:
            # Ask the user for the time to check the status of the packages
            time_input = input("Enter a time in the following format for status of packages, HH:MM:SS ")
            hours, minutes, seconds = map(int, time_input.split(":"))
            input_time = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)

            # User package check choice
            package_choice = input("Enter 'all' to see all the package info, or enter 'one' to enter the package id "
                                   "and find the single package")

            if package_choice == "one":
                # Ask the user for the package ID
                package_id_input = input("Which package are you looking for? Enter package ID #")
                # Get the package and adjust its delivery status
                package = package_hash_table.get(int(package_id_input))
                package.adjust_delivery_status(input_time)
                # Print the package's information
                print(str(package))
            elif package_choice == "all":
                # For each package ID, get the package and adjust its delivery status
                for package_id in range(1, 41):
                    package = package_hash_table.get(package_id)
                    package.adjust_delivery_status(input_time)
                    # Print the package's information
                    print(str(package))
            else:
                return
        except ValueError:
            print("Entry invalid. Closing program.")
            return


def main():
    WGUPSProgram.start()


if __name__ == "__main__":
    main()

import csv

from Hash_Table import HashTable
from Package import Package


def loadPackageData(hash_table):
    with open('Data/packages.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            # CSV columns: Package ID, Address, City, State, Zip code, Deliver Deadline, Weight
            id = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = row[4]
            deadline = row[5]
            weight = row[6]
            special_note = row[7]
            status = "At hub"  # Initial status for all packages
            # Create Package object and insert into HashTable
            package = Package(id, address, deadline, city, state, zip_code, weight, special_note, status)
            hash_table.insert(id, package)


# Create a hash table
hash_table = HashTable()

# Load packages from CSV into hash table
loadPackageData(hash_table)

# Print details of all packages
for i in range(1, 41):  # Assuming package IDs are from 1 to 40
    package = hash_table.lookup(i)
    if package:
        print(str(package))
    else:
        print(f"Package with ID {i} not found.")


def loadDistanceData():
    distanceData = []
    with open('Data/distances.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            # Convert each distance to a float, and append the result to distanceData
            distanceRow = [float(distance) if distance else None for distance in row]
            distanceData.append(distanceRow)
    return distanceData


distanceData = loadDistanceData()

for distance in distanceData:
    print(distance)

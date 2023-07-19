# Example file for Advanced Python: Working With Data by Joe Marini
# read data from a CSV file into an object structure

import csv
import pprint


# read the contents of a CSV file into an object structure
result = []

# TODO: open the CSV file for reading
with open("file.csv", "r") as csvfile:
    reader = csv.reader(csvfile)

with open("file.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        print(row)
        result.append(row)

pprint.pp(result)

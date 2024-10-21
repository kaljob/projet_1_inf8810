import sys
import csv

# Read from Standard Input
reader = csv.reader(sys.stdin)

next(reader, None) # Skip the header

for row in reader:
    try:
        host_location = row[6]
        price = row[15]
        print("%s\t%s"%(host_location, price))
    except ValueError:
        continue
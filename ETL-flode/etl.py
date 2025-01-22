"""Skap ett ETL-flöde"""

import csv  
with open ("KIR-data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
#import necessary modules
import csv

reader = csv.DictReader(open("file2.csv"))
for raw in reader:
    print(raw)
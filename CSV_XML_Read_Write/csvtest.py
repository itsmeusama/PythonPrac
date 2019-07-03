import csv

with open('sample.csv','r') as csv_data:
    csv_reader = csv.reader(csv_data)
    
    for line in csv_reader:
        print (line)
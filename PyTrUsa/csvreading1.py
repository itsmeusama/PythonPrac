import csv
#Readung a CSV using CSV Library
with open('csvsample.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} Lives in {row["city"]} , and age is: {row["row[2]"}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
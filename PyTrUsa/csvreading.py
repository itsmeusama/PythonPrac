import csv
#Reading a CSV File

with open('csvsample.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} Lives in {row[1]}, He is: {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
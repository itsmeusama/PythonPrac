import csv
#Write To CSV/Notepad 
#https://realpython.com/python-csv/  #Refer

with open('csvsample2.txt', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['Alex', 'Eng', 'June'])
    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
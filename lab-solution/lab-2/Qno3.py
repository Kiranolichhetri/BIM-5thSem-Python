# WAP that reads data from emp.csv file and displays content of column 0, 1, and 3.

import csv

def read_emp_csv(filename):
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row[0], row[1], row[3])

# Specify the filename
filename = 'emp.csv'

# Call the function to read and display the content of specified columns
read_emp_csv(filename)

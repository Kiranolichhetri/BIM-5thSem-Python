# WAP that reads columns 1,2, and 3 from emp.csv file and converts them into list
# of tuples where elements of the tuple are from column 1, 2, and 3 respectively.


import csv

def read_and_convert_to_tuples(filename):
    tuples_list = []
    with open(filename, mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # Assuming the CSV has at least 4 columns
            if len(row) > 3:
                tuples_list.append((row[1], row[2], row[3]))
    return tuples_list

# Specify the filename
filename = 'emp.csv'

# Call the function and print the list of tuples
tuples_list = read_and_convert_to_tuples(filename)
print(tuples_list)

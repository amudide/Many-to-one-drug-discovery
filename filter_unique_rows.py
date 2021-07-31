from csv import reader
import csv

read_in = 'correlation-analysis-all.csv'
read_out = 'correlation_filtered-all.csv'

header = None

with open(read_in, 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        header = row
        break

with open(read_out, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)

flag = True

rows = []

with open(read_in, 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        if flag:
            flag = False
            continue

        string = "".join(row)
        if string not in rows:
            rows.append(string)
            with open(read_out, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(row)

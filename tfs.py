from csv import reader
import requests
import csv
import ssl

read_in = 'TFs_Model_EGT-vs-Model.csv'
read_out = 'tfs.csv'

with open(read_out, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["TFs", "Group", "Gene"])

flag = True

with open(read_in, 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        if flag:
            flag = False
            continue
        tf = row[0]
        group = row[1]
        gene_number = int(row[2])
        genes = row[3]

        gene_list = []

        if (group == "Up" or group == "Down") and gene_number > 0:
            gene_list = genes.split(";")

        for i in gene_list:
            with open(read_out, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([tf, group, i])
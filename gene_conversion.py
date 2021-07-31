from csv import reader
import requests
import csv

read_in = 'Model_EGT-vs-Model-all.gene.csv'
read_out = 'prospective_protein_matches_all.csv'
"""
with open(read_out, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["UNIPROT ID", "GENE", "From Docking List", "Docking Rank", "From Raw Data", "GO ID", "P-Value Significance", "Fold Change"])
"""

with open(read_in, 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        gene = row[0]
        protein = row[20]
        go_id = row[23]
        pval = row[6]
        fold_change = row[4]

        print(gene)

        fullURL = ('http://www.uniprot.org/uniprot/?query=organism%3A10090+AND+gene%3A' + str(gene) + '&format=tab&columns=id,protein%20names')

        result = requests.get(fullURL)

        lines = result.text.split('\n')

        for i in lines[1:-1]:
            cells = i.split("\t")
            entry = cells[0]
            protein_guessed = cells[1]

            with open("cumulative-results.csv", "rt") as f:
                csvreader = csv.reader(f, delimiter=",")
                for row in csvreader:
                    if entry in row[3]:
                        with open(read_out, 'a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow([entry, gene, protein, row[0], protein_guessed, go_id, pval, fold_change])
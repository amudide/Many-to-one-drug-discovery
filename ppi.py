from csv import reader
import csv

read_in_ppi = 'diff-Model_EGT-vs-Model_gene2gene_network.txt'
read_in_genes = 'prospective_protein_matches.csv'
read_out = 'ppi.csv'

with open(read_out, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["gene_docked", "gene_type", "other_gene", "gene_type", "combined_score"])

flag = True

with open(read_in_ppi, 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        if flag:
            flag = False
            continue
        row = row[0].split("\t")
        gene1 = row[0]
        gene_type1 = row[1]
        gene2 = row[2]
        gene_type2 = row[3]
        combined_score = row[4]

        with open(read_in_genes, 'r') as read_genes:
            csv_genes = reader(read_genes)
            for row_genes in csv_genes:
                if row_genes[1] == gene1:
                    with open(read_out, 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([gene1, gene_type1, gene2, gene_type2, combined_score])
                elif row_genes[1] == gene2:
                    with open(read_out, 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([gene2, gene_type2, gene1, gene_type1, combined_score])

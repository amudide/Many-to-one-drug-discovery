from csv import reader
import csv

read_in_docking = 'prospective_protein_matches_all.csv'
read_in_all = 'prospective_protein_matches_all.csv'
read_in_docking_results = 'cumulative-results.csv'
read_out = 'correlation-analysis-all.csv'

with open(read_out, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["UNIPROT ID", "Protein Name", "Docking Rank", "Docking Affinity", "Gene Rank", "Gene P-Value Significance", "Fold Change"])

with open(read_in_docking, 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        uniprot = row[0]
        protein = row[2]
        docking_rank = row[3]
        gene_rank = row[6]

        docking_affinity = ""

        with open(read_in_docking_results, "rt") as f:
            csvreader = csv.reader(f, delimiter=",")

            for row in csvreader:
                if uniprot == row[3] and docking_rank == row[0]:
                    docking_affinity = row[2]

        with open(read_in_all, "rt") as f:
            csvreader = csv.reader(f, delimiter=",")
            for row in csvreader:
                if uniprot == row[0] and row[3] == docking_rank:
                    pval = row[6]
                    foldchange = row[7]
                    with open(read_out, 'a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([uniprot, protein, docking_rank, docking_affinity, gene_rank, pval, foldchange])
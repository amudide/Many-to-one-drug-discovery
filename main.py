import json
import wget
from rcsbsearch import Attr
import csv


def download(path):
    url_download = "https://files.rcsb.org/download/" + assemblyid + ".pdb"
    wget.download(url_download, path + assemblyid + '.pdb')


with open('mobidb_result.json') as data_file:
    data = json.load(data_file)

with open('jobs-sruthi.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["", "protein_file", "start", "end", "acc", "name"])

row_num = 1

for i in data:

    results = Attr(
        "rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_accession").exact_match(
        i["acc"]) \
        .and_("rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_name").exact_match(
        "UniProt") \
        .and_("rcsb_entry_info.polymer_entity_count_protein").equals(1) \
        .exec("entry")

    is_found = False

    final_assembly_id = None

    for assemblyid in results:
        is_found = True
        download('/Users/sruthikurada/Documents/MIT PRIMES/Ergothionine/')
        final_assembly_id = assemblyid
        break

    if not is_found:
        results = Attr(
            "rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_accession").exact_match(
            i["acc"]) \
            .and_("rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_name").exact_match(
            "UniProt") \
            .exec("entry")

        for assemblyid in results:
            is_found = True
            download('/Users/sruthikurada/Documents/MIT PRIMES/Ergothionine/')
            final_assembly_id = assemblyid
            break

        protein_file = final_assembly_id + '.pdb'
        start = 1
        end = i["length"]
        acc = i["acc"]
        name = i["name"]

        with open('jobs-sruthi.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([row_num, protein_file, start, end, acc, name])

        row_num += 1

import json
import wget
from rcsbsearch import Attr
import pickle


def download(path):
    url_download = "https://files.rcsb.org/download/" + assemblyid + ".pdb"
    wget.download(url_download, path + assemblyid + '.pdb')


with open('mobidb_result.json') as data_file:
    data = json.load(data_file)

dict = {}

total = 0
found = 0

for i in data:
    results = Attr(
        "rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_accession").exact_match(
        i["acc"]) \
        .and_("rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_name").exact_match(
        "UniProt") \
        .and_("rcsb_entry_info.polymer_entity_count_protein").equals(1) \
        .exec("entry")

    dict[i["acc"]] = []

    total += 1

    is_found = False

    for assemblyid in results:
        found += 1
        is_found = True
        download('/Users/sruthikurada/Documents/MIT PRIMES/Ergothionine/')

        dict[i["acc"]].append(assemblyid)

        break

    if not is_found:
        results = Attr(
            "rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_accession").exact_match(
            i["acc"]) \
            .and_("rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_name").exact_match(
            "UniProt") \
            .exec("entry")

        for assemblyid in results:
            found += 1

            download('/Users/sruthikurada/Documents/MIT PRIMES/Ergothionine/')

            dict[i["acc"]].append(assemblyid)

            break

print(found / total)

# This saves your dict
with open('id_to_file.p', 'bw') as f:
    pickle.dump(dict, f)

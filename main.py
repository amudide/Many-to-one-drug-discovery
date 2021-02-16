import json
import wget
from rcsbsearch import Attr
import pickle

with open('mobidb_result.json') as data_file:
    data = json.load(data_file)

dict = {}

for i in data:
    print(i["acc"])

    results = Attr(
        "rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_accession").exact_match(
        i["acc"]) \
        .and_("rcsb_polymer_entity_container_identifiers.reference_sequence_identifiers.database_name").exact_match(
        "UniProt") \
        .exec("entry")

    dict[i["acc"]] = []

    for assemblyid in results:
        print(assemblyid)

        url_download = "https://files.rcsb.org/download/" + assemblyid + ".pdb"
        wget.download(url_download, '/Users/sruthikurada/Documents/MIT PRIMES/Ergothionine/' + assemblyid + '.pdb')

        dict[i["acc"]].append(assemblyid)


# This saves your dict
with open('id_to_file.p', 'bw') as f:
    pickle.dump(dict, f)
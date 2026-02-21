import argparse
from Bio import Entrez, SeqIO
from src.logic import get_seq_from_id

Entrez.mail = "tauzin_pierre@orange.fr"

parser = argparse.ArgumentParser()
parser.add_argument("--id")
args = parser.parse_args()
id_seq = args.id

record = get_seq_from_id(id_seq)

name = record.description
start_seq = record.seq.find("ATG")

cds_seq = record.seq[start_seq:]

prot_seq = cds_seq.translate(to_stop=True)
prot_length = len(prot_seq)

index_stop = start_seq + (prot_length * 3) + 3

print(f"Description : {name}")
print(f"Début (ATG) : {start_seq}")
print(f"Fin (Stop)  : {index_stop}")
print(f"Longueur de la protéine : {prot_length} acides aminés")

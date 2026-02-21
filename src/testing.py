from Bio import Entrez, SeqIO
from src.logic import get_seq_from_id

Entrez.mail = "tauzin_pierre@orange.fr"

record = get_seq_from_id("NC_001416.1")

nb_g = record.seq.count("G")
nb_c = record.seq.count("C")
nb_A = record.seq.count("A")
nb_T = record.seq.count("T")

gc_percent = (nb_c + nb_g) / (nb_g + nb_c + nb_A + nb_T)

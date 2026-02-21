from Bio import Entrez, SeqIO


def get_seq_from_id(id_seq):
    with Entrez.efetch(
        db="nucleotide", id=id_seq, rettype="gb", retmode="text"
    ) as handle:
        return SeqIO.read(handle, "genbank")

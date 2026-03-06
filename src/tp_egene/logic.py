from Bio import Entrez
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()


class seq_reverser_transcripter:
    """
    Fonction permettant de faire de la transcription et de la réversion de séquence, ainsi que d'en output un fichier fasta
    """

    def __init__(self, seq):
        self.seq = seq.lower()
        self.validation
        self.seq_list = [letter for letter in self.seq]

    @property
    def validation(self):
        """
        Permet de valider le format de la séquence d'input
        """
        assert all(base in "atcg" for base in self.seq)

    def dna(self):
        """
        Permet de manipuler l'objet séquence brut
        """
        dna = self.seq
        return dna

    def reverse_dna(self):
        """
        Permet de reverse une séquence
        """
        reverse_list = self.seq_list[::-1]
        reverse = "".join(reverse_list)
        return reverse

    def transcribe_dna(self):
        """
        Permet de transcrire une séquence
        """
        ref = {"a": "t", "g": "c", "t": "a", "c": "g"}
        comp_list = [ref[letter] for letter in self.seq_list]
        complementary = "".join(comp_list)
        return complementary

    def reverse_transcription(self):
        """
        Permet d'obtenir le transcrit inverse d'une séquence
        """
        p1 = self.transcribe_dna()
        p2 = p1[::-1]
        return p2


def import_seq_from_ncbi_id(id_ncbi):
    Entrez.email = os.getenv("NCBI_EMAIL")

    if not Entrez.email:
        print("absence d'email pour le ncbi dans le .env")
        return None

    with Entrez.efetch(
        db="nucleotide", id=id_ncbi, rettype="fasta", retmode="text"
    ) as handle:
        row_data = handle.read().strip()
    return row_data


def export_datas(id, desc, seq):
    subprocess.run(["bash", "tp_egene/export.sh", id, desc, seq])


def parser_ncbi(raw_data):
    decomposed = raw_data.split("\n")
    header = decomposed[0]
    header_list = header.split(" ")

    seq = decomposed[1]
    id_seq = "".join(header_list[0])
    desc = " ".join(header_list[1:])

    return id_seq, desc, seq


# def recup_seq():
#     type_import = sys.argv[1]
#
#     if type_import == "ncbi":
#         id_ncbi = sys.argv[2]
#         return id_ncbi
#
#     elif type_import == "seq":
#         id_seq = sys.argv[2]
#         desc_seq = sys.argv[3]
#         seq = sys.argv[4]
#         return id_seq, desc_seq, seq
#
#     else:
#         print("Erreur : Nommbre d'arguments incorrect")

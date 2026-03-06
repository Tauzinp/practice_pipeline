import sys
from logic import import_seq_from_ncbi_id
from logic import parser_ncbi
from logic import export_datas
from logic import seq_reverser_transcripter
# NC_001416.1

id_ncbi = sys.argv[2]

raw_data = import_seq_from_ncbi_id(id_ncbi)

parsed_data = parser_ncbi(raw_data)

id_seq = parsed_data[0]
desc = parsed_data[1]
seq = parsed_data[2]


analyser = seq_reverser_transcripter(seq)

dna = analyser.dna()
print(f"Voici la séquence d'adn brute : {dna}")

reversed = analyser.reverse_dna()
print(f"Voici la séquence reversed : {reversed}")

transcript = analyser.transcribe_dna()
print(f"Voici la séquence transcrite : {transcript}")

reversed_transcript = analyser.reverse_transcription()
print(f"Voici la séquence reversed et transcrite : {reversed_transcript}")

choices = ["1", "2", "3", "4"]
sortie = input(
    "Quel fichier souhaitez-vous garder ? 1-dna  2-reversed  3-transcript  4-reversed transcript"
)

if sortie == "1":
    seq_out = dna
elif sortie == "2":
    seq_out = reversed
elif sortie == "3":
    seq_out = transcript
else:
    seq_out = reversed_transcript

while True:
    if sortie in choices:
        export_datas(id_seq, desc, seq_out)
        break
    else:
        print(f"{sortie} n'est pas un choix valide")
        break

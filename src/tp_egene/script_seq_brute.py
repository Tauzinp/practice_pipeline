import sys
from logic import seq_reverser_transcripter
from logic import export_datas


id_seq = sys.argv[2]
desc = sys.argv[3]
seq = sys.argv[4]

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

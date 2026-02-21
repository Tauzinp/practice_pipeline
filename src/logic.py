from Bio import Entrez, SeqIO
import plotext as plt


def get_seq_from_id(id_seq):
    Entrez.mail = "tauzin_pierre@orange.fr"

    with Entrez.efetch(
        db="nucleotide", id=id_seq, rettype="gb", retmode="text"
    ) as handle:
        return SeqIO.read(handle, "genbank")


def get_gc_percent(seq):
    seq = seq.upper()

    if len(seq) == 0:
        return print("Séqeunce vide")

    nb_g = seq.count("G")
    nb_c = seq.count("C")

    gc_percent = (nb_c + nb_g) / len(seq)
    return gc_percent


def draw_gc_graph(seq, window_size=500):
    gc_values = []
    position = []

    for i in range(0, len(seq), window_size):
        segment = seq[i : i + window_size]

        score = get_gc_percent(segment)

        gc_values.append(score)
        position.append(i)

    plt.clf()
    plt.plot(position, gc_values, color="orange")

    plt.title("Variation du contenu en GC (Fenêtres de 500bp)")
    plt.xlabel("Position sur le génome (bp)")
    plt.ylabel("% GC")

    global_mid = get_gc_percent(seq)
    plt.hline(global_mid, color="red")

    plt.show()

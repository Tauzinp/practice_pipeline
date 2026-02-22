from Bio import Entrez, SeqIO
from src.logic import draw_cumulated_skew, get_seq_from_id
from src.logic import draw_gc_graph
from src.logic import get_skew_value
from src.logic import draw_gc_skew
from src.logic import draw_cumulated_skew

record = get_seq_from_id("NC_001416.1")

gc_graph = draw_gc_graph(record.seq)

skew_graph = draw_gc_skew(record.seq)

skew_graph_cumulated = draw_cumulated_skew(record.seq)


def count_kmers(seq, k=4):
    frequency = {}
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i : i + k]

        if subseq in frequency:
            frequency[subseq] += 1

        else:
            frequency[subseq] = 1

    return frequency


test = count_kmers(record.seq, k=4)
print(test)

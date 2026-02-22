from Bio import Entrez, SeqIO
from src.logic import get_seq_from_id
from src.logic import draw_gc_graph
from src.logic import get_skew_value
from src.logic import draw_skew_graph

record = get_seq_from_id("NC_001416.1")

gc_graph = draw_gc_graph(record.seq)

gc_skew = get_skew_value(record.seq)
print(gc_skew)

skew_graph = draw_skew_graph(record.seq)

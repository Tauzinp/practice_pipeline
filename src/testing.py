import plotext as plt
from Bio import Entrez, SeqIO
from src.logic import count_kmers, draw_cumulated_skew, get_seq_from_id
from src.logic import draw_gc_graph
from src.logic import get_skew_value
from src.logic import draw_gc_skew
from src.logic import draw_cumulated_skew
from src.logic import count_kmers
from src.logic import get_distribution_kmer
from src.logic import draw_kmer_graph
from src.logic_poo import GCAnalyser

record = get_seq_from_id("NC_001416.1")

gc_graph = draw_gc_graph(record.seq)

skew_graph = draw_gc_skew(record.seq)

skew_graph_cumulated = draw_cumulated_skew(record.seq)

kmer_counts = count_kmers(record.seq)
kmer_distribution = get_distribution_kmer(kmer_counts)
kmer_graph = draw_kmer_graph(kmer_distribution)

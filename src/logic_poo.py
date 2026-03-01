class GCAnalyser:
    def __init__(self, seq):
        self.seq = seq
        self.seq = self.seq.upper()
        self.segment_values()

    def get_percent(self, segment=None):
        target = segment if segment is not None else self.seq

        if len(target) == 0:
            raise ValueError("Séquence vide")

        nb_g = target.count("G")
        nb_c = target.count("C")

        gc_percent = (nb_c + nb_g) / len(target)
        return gc_percent

    def segment_values(self, window_size=500):
        gc_values = []
        position = []

        for i in range(0, len(self.seq), window_size):
            segment = self.seq[i : i + window_size]

            score = self.get_percent(segment)

            gc_values.append(score)
            position.append(i)

        self.gc_values = gc_values
        self.position = position

    def draw_gc(self, plt):
        plt.clf()
        plt.theme("dark")

        plt.plot(self.position, self.gc_values)

        plt.title("Variation")
        plt.xlabel("Position sur le génome (bp)")
        plt.ylabel("% GC")

        global_mid = self.get_percent()

        plt.hline(global_mid, color="red")


class gcSkewAnalyser:
    def __init__(self, seq):
        self.seq = seq
        self.seq = self.seq.upper()
        self.segment_values()

    def get_skew(self, segment=None):
        target = segment if segment is not None else self.seq
        if len(self.seq) == 0:
            return print("Séquence vide")

        nb_g = target.count("G")
        nb_c = target.count("C")

        gc_skew = (nb_g - nb_c) / (nb_g + nb_c)
        return gc_skew

    def segment_values(self, window_size=500):
        position = []
        cumulated_skew_values = []
        current_total = 0

        for i in range(0, len(self.seq), window_size):
            segment = self.seq[i : i + window_size]

            score = self.get_skew(segment)

            current_total += score or 0
            position.append(i)
            cumulated_skew_values.append(current_total)

        self.position = position
        self.skew_segment_values = cumulated_skew_values

    def draw_gc_skew(self, plt):
        plt.clf()
        plt.theme("dark")

        plt.plot(self.position, self.skew_segment_values, color="orange")

        plt.title("GC Skew en cumulé")
        plt.xlabel("Position sur le génome (bp)")
        plt.ylabel("Proportion")

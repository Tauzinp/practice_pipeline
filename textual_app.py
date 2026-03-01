from textual.app import App
from textual.widgets import Header, Footer, Label, Static, Button, Input
from textual_plotext import PlotextPlot

import plotext as plt

from src.logic import get_seq_from_id
from src.logic_poo import GCAnalyser


class MonApp(App):
    BINDINGS = [("q", "quit", "Quitter")]
    CSS = """
    #static_descritpion, #static_seq {
        height: auto;
        margin: 0 1;
    }

    /* Le graphique prend tout l'espace disponible (1fr) */
    #static_gc_graph {
        height: 1fr; 
        min-height: 20;
        border: tall grey;
        background: black;
        margin: 1;
    }
    """

    def compose(self):
        yield Header()
        yield Input(placeholder="NCBI ID", id="input_id")
        yield Button("Importer la séquence", id="btn_import", variant="success")
        yield Static("Résultats", id="static_descritpion")
        yield Static("Séquence", id="static_seq")
        yield Button("Tracer le Graphique des GC", id="btn_graph", variant="success")
        yield PlotextPlot(id="static_gc_graph")
        yield Footer()

    def on_button_pressed(self, event):
        if event.button.id == "btn_import":
            self.gerer_importation()
        elif event.button.id == "btn_graph":
            self.gerer_graphique()

    def gerer_importation(self):
        champ_saisie = self.query_one("#input_id")
        display_zone_description = self.query_one("#static_descritpion")
        display_zone_seq = self.query_one("#static_seq")

        id_seq = champ_saisie.value

        if not id_seq:
            display_zone_description.update("Veuillez entrer un ID")
            return

        try:
            self.record = get_seq_from_id(id_seq)

            display_zone_description.update(str(self.record.description))
            display_zone_seq.update(str(self.record.seq)[:500])
        except Exception as e:
            display_zone_description.update(f"Erreur : {e}")

    def gerer_graphique(self):
        graph_widget = self.query_one("#static_gc_graph", PlotextPlot)

        if hasattr(self, "record"):
            try:
                plt = graph_widget.plt

                analyser = GCAnalyser(str(self.record.seq))
                analyser.segment_values()

                analyser.draw_gc(plt)
                graph_widget.refresh()

            except Exception as e:
                self.notify(f"Erreur : {e}", severity="error")
        else:
            self.notify("Importez une séquence d'abord !", severity="warning")


if __name__ == "__main__":
    app = MonApp()
    app.run()

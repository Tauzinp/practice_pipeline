from textual.app import App
from textual.widgets import Header, Footer, Label, Static, Button, Input

import plotext as plt

from src.logic import get_seq_from_id
from src.logic_poo import GCAnalyser


class MonApp(App):
    BINDINGS = [("q", "quit", "Quitter")]
    CSS = """
    #static_action {
        margin: 1 0;
        padding: 1;
        border: solid green;
    }

    /* On donne une vraie taille à la zone du graphique */
    #static_gc_graph {
        height: 20;           /* 20 lignes de haut */
        width: 100%;          /* Toute la largeur */
        border: tall grey;    /* Une bordure pour bien voir la zone */
        background: black;
    }
    """

    def compose(self):
        yield Header()
        yield Input(placeholder="NCBI ID", id="input_id")
        yield Button("Importer la séquence", id="btn_import", variant="success")
        yield Static("Résultats", id="static_descritpion")
        yield Static("Séquence", id="static_seq")
        yield Button("Tracer le Graphique des GC", id="btn_graph", variant="success")
        yield Static("GC Graph", id="static_gc_graph")
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
        display_zone_gc_graph = self.query_one("#static_gc_graph")

        if hasattr(self, "record"):
            try:
                largeur = display_zone_gc_graph.content_size.width
                hauteur = display_zone_gc_graph.content_size.height

                analyser = GCAnalyser(str(self.record.seq))
                analyser.segment_values()

                analyser.draw_gc(width=largeur, height=hauteur - 2)
                graph_text = plt.build()
                display_zone_gc_graph.update(graph_text)

            except Exception as e:
                display_zone_gc_graph.update(f"Erreur : {e}")
        else:
            display_zone_gc_graph.update("Importez une séquence d'abord !")


if __name__ == "__main__":
    app = MonApp()
    app.run()

from textual.app import App
from textual.widgets import Header, Footer, Label, Static, Button, Input

from src.logic import get_seq_from_id


class MonApp(App):
    BINDINGS = [("q", "quit", "Quitter")]
    CSS = """
    #static_action {
        margin: 1 0;
        padding: 1;
        border: solid green;
    }
    """

    def compose(self):
        yield Header()
        yield Input(placeholder="NCBI ID", id="input_id")
        yield Button("Importer la séquence", id="btn_import", variant="success")
        yield Static("Résultats", id="static_descritpion")
        yield Static("Séquence", id="static_seq")
        yield Footer()

    def on_button_pressed(self, event):
        champ_saisie = self.query_one("#input_id")
        id_seq = champ_saisie.value

        display_zone_description = self.query_one("#static_descritpion")
        display_zone_seq = self.query_one("#static_seq")

        if id_seq:
            display_zone_description.update("Recherche en cours")
            display_zone_seq.update("")

            try:
                record = get_seq_from_id(id_seq)
                description = str(record.description)
                display_zone_description.update(description)

                sequence = str(record.seq)
                seq_500 = sequence[:500]
                display_zone_seq.update(seq_500)

            except Exception as e:
                display_zone_description.update(f"Erreur : {e}")
                display_zone_seq.update("")

        else:
            display_zone_description.update(
                "Veuillez entrer l'id de la séquence à analyser"
            )
            display_zone_seq.update("")


if __name__ == "__main__":
    app = MonApp()
    app.run()

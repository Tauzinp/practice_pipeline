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
        yield Static("Résultats", id="static_result")
        yield Footer()

    def on_button_pressed(self, event):
        champ_saisie = self.query_one("#input_id")
        id_seq = champ_saisie.value

        display_zone = self.query_one("#static_result")

        if id_seq:
            display_zone.update("Recherche en cours")

            try:
                record = get_seq_from_id(id_seq)
                description = str(record.description)
                display_zone.update(description)
            except Exception as e:
                display_zone.update(f"Erreur : {e}")

        else:
            display_zone.update("Veuillez entrer l'id de la séquence à analyser")


if __name__ == "__main__":
    app = MonApp()
    app.run()

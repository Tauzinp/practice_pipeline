from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from src.logic import draw_kmer_graph


class KmerGraphWidget(Static):
    """Widget qui encapsule ton graphique."""

    def __init__(self, data, **kwargs):
        super().__init__(**kwargs)
        self.data = data

    def on_mount(self) -> None:
        """S'exécute quand le widget est affiché."""
        width = self.size.width
        height = self.size.height - 2

        # On appelle ta fonction modifiée
        graph_text = draw_kmer_graph(self.data, width, height)

        # On met à jour le widget avec le graph
        self.update(graph_text)


class SeqCuriosity(App):
    CSS = """
    KmerGraphWidget {
        border: rounded $accent;
        padding: 1;
        margin: 1;
        width: 100%;
        height: 100%;
    }
    """

    def compose(self) -> ComposeResult:
        fake_data = ([i for i in range(50)], [1 / i if i > 0 else 0 for i in range(50)])

        yield Header()
        yield KmerGraphWidget(data=fake_data)
        yield Footer()


if __name__ == "__main__":
    app = SeqCuriosity()
    app.run()

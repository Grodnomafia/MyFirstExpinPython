from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.reactive import reactive
from textual.widgets import Markdown


class NoteViewWidget(VerticalScroll):
    text:reactive[str | None] =reactive('')

    def compose(self) -> ComposeResult:
        yield Markdown('faafa')

    def watch_text(self,_:str,new_text:str)->None:
        self.query_one(Markdown).update(new_text)
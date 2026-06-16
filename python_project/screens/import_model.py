import httpx
from textual.screen import  ModalScreen
from textual.containers import Container, Horizontal
from textual.widgets import Static,Input,Button



class ImportModal(ModalScreen[str]):
    CSS = """
    #dialog {
        border: solid grey;
        }
    #title {
        dock: top;
        content-align:  center middle;
        padding: 0 1;
        height: 2;
        }
    #buttons {
        align: center middle;
        }
    
    """

    def compose(self):
        with Container():
            yield Static("Импорт данных",id='title')
            yield Input(placeholder="Введите url для импорта",id='import-url')
            with Horizontal(id="buttons"):
                yield Button("Импортировать",variant="primary",id="import-btn")
                yield Button("Отмена",id="cancel-btn")
    def on_button_pressed(self,event : Button.Pressed)->None:
        if event.button.id == "import-btn":
            url_input = self.query_one("#import-url",Input)
            url = url_input.value.strip()
            if url:
                self.app.call_later(self.import_data, url)
            else:
                url_input.styles.border = ("solid","red")
        else:
            self.dismiss(None)


    async  def import_data(self,url:str)->None:
        try:
            async  with httpx.AsyncClient(timeout=10.0) as client:
                response = await  client.get(url)
                response.raise_for_status()
                data = response.text
                self.dismiss(data)
        except httpx.HTTPError as e:
            self.app.notify(f'Ошибка загрузки {e}',severity='error')
        except Exception as e:
            self.app.notify(f'Неизвестная ошибка {e}',severity='error')
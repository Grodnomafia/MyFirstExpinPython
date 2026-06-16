from textual.app import App
from .config import AppSettings
from python_project.repositories import FolderRepository,NoteRepository
from .screens import MainScreen


class NoteManagerApp(App):
    def __init__(self, settings: AppSettings, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings = settings

    def on_mount(self) -> None:
        folder_repo = FolderRepository(self.settings.data_directory)
        note_repo = NoteRepository(self.settings.data_directory)
        main_screen = MainScreen(self.settings,folder_repo,note_repo)
        self.push_screen(main_screen)

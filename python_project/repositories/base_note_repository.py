from abc import ABC,abstractmethod
from python_project.domain import Note
from pathlib import Path
from typing import Optional

class BaseNoteRepository(ABC):
    @abstractmethod
    def get_notes_by_path(self,path: Path) -> list[Note]:
        pass
    @abstractmethod
    def create_note(self, path: Path,name: str,content:str) -> Note:
        pass

    @abstractmethod
    def delete_note(self, note: Note) -> None:
        pass

    @abstractmethod
    def update_note(self,note:Note,content:str,new_name:Optional = None)->Note:
        pass
    @abstractmethod
    def load_note(selfm,path:Path)->Note:
        pass
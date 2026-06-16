from abc import ABC,abstractmethod
from python_project.domain import Folder
from pathlib import Path


class BaseFolderRepository(ABC):
    @abstractmethod
    def get_folder_by_path(self,path: Path) -> list[Folder]:
        pass
    @abstractmethod
    def create_folder(self, path: Path,name: str) -> Folder:
        pass

    @abstractmethod
    def delete_folder(self, folder: Folder) -> None:
        pass
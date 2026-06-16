import shutil
from pathlib import Path
from python_project.domain.folder import Folder
from python_project.repositories.base_folder_repository import BaseFolderRepository


class FolderRepository(BaseFolderRepository):
    def __init__(self,base_path):
        self.base_path = base_path.resolve()

    def _check_path(self,path: Path):
        '''Проверка пути'''
        if not path.exists() or not path.is_dir():
            raise ValueError(f'Folder doent exist: {path}')

        if self.base_path not in path.parents and path != self.base_path:
            raise ValueError('Access outside data directory in not allowed')

    def get_folder_by_path(self,path: Path) -> list[Folder]:
        '''Получения деректории'''
        path = path.resolve()
        self._check_path(path)


        folders : list[Folder] = []
        for sub_path in path.iterdir():
            if sub_path.is_dir() and not sub_path.name.startswith('.'):
                folders.append(
                    Folder(
                    name= sub_path.name,
                    path = sub_path)
                )
        return sorted(folders,key=lambda f: f.name)

    def create_folder(self, path: Path, name: str) -> Folder:
        '''Создание директории'''
        self._check_path(path)
        if not name or '/' in name or '\\' in name:
            raise ValueError('Invalid folder name')
        path.mkdir(parents=True,exist_ok=False)
        return Folder(name=name,path=path)

    def delete_folder(self, folder: Folder) -> None:
        '''Удаление деректории'''
        path = folder.path.resolve()
        self._check_path(path)
        if path == self.base_path:
            raise ValueError("can't delete base path")
        shutil.rmtree(path)



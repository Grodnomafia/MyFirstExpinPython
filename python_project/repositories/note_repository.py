from importlib.resources import contents
from pathlib import Path
from python_project.domain import Note
from python_project.repositories.base_note_repository  import BaseNoteRepository
from typing import Optional


class NoteRepository(BaseNoteRepository):
    def __init__(self,base_path):
        self.base_path = base_path.resolve()

    def _check_path(self, path: Path):
        '''Проверка пути - должен быть внутри base_path'''
        # Преобразуем проверяемый путь в абсолютный
        abs_path = path.resolve()

        # Проверяем, существует ли путь и является ли директорией
        if not abs_path.exists():
            raise ValueError(f'Path does not exist: {path}')

        if not abs_path.is_dir():
            raise ValueError(f'Path is not a directory: {path}')

        # Проверяем, находится ли путь внутри base_path
        try:
            # Пытаемся получить относительный путь относительно base_path
            abs_path.relative_to(self.base_path)
        except ValueError:
            # Если не получилось - значит путь вне разрешенной директории
            raise ValueError(f'Access outside data directory is not allowed: {path}')

    def get_notes_by_path(self,path: Path) -> list[Note]:
        '''Получения заметок'''
        path = path.resolve()
        self._check_path(path)


        notes : list[Note] = []
        for sub_path in path.iterdir():
            if sub_path.is_file() and not sub_path.name.startswith('.') and sub_path.suffix == '.md':
                notes.append(
                    Note(
                    name= sub_path.name,
                    path = sub_path)
                )
        return sorted(notes,key=lambda f: f.name)

    def create_note(self, path: Path, name: str,content:str) -> Note:
        '''Создание заметок'''
        self._check_path(path)
        if not name or '/' in name or '\\' in name:
            raise ValueError('Invalid note name')
        new_path = path / f'{name}.md'
        new_path.write_text(content,encoding='utf-8')

        return Note(name=name,path=path)

    def delete_note(self, note: Note) -> None:
        '''Удаление заметок'''
        path = note.path.resolve()

        path.unlink()

    def update_note(self, note: Note, content: str, new_name: Optional = None)->Note:
        """Обновление заметки"""
        path = note.path.resolve()
        self._check_path(path)

        path.write_text(content,encoding='utf-8')

        if new_name and new_name != note.name:
            if '/' in new_name or '\\' in new_name:
                raise ValueError('Invalid Note Name')
            new_path = path.parent / f"{new_name}.md"
            path.rename(new_path)
            return Note(new_name,new_path)
        return note

    def load_note(selfm,path:Path) ->Note:
        with open(path,"r",encoding="utf-8") as f:
            content = f.read()
            return Note(
                path.name,
                path,
                content
            )
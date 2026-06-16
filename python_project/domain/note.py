from dataclasses import dataclass
from pathlib import Path
from datetime import datetime
from typing import Optional



@dataclass
class Note:
    name: str
    path: Path
    content : Optional[str] = ""
    created_at : Optional[datetime] = datetime.now()
    updated_at : Optional[datetime] =datetime.now()

    def __post_init__(self):
        if not self.name or self.name.strip() == '':
            raise ValueError('Note must have name')
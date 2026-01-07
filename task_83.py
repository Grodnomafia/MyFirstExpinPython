import os
from typing import Optional, TextIO


class File:
    def __init__(self,path:str,mode:str,encod:str)->None:
        self.path = path
        self.mode = mode
        self.encod = encod
        self.file: Optional[TextIO] = None

    def __enter__(self)->TextIO:
        try:
            self.file = open(self.path,self.mode,encoding=self.encod)
        except (FileNotFoundError,PermissionError,UnicodeError) as y:
            if 'r' in self.mode or 'a' in self.mode:
                os.makedirs(os.path.dirname(self.path), exist_ok=True)
                self.file = open(self.path,'w',encoding= self.encod)
                self.file.write('Записал тут текст')
                self.file = open(self.path, 'r', encoding=self.encod)
            else:
                self.file = open(self.path,self.mode,encoding=self.encod)
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file and not self.file.closed:
            self.file.close()
        return True



with File('D:\\exp2\\7.txt','r','utf-8') as x:
    print(x.read())
from typing import Protocol

class Storage(Protocol):
    def save(self,data:str)->None:
        pass
    def load(self)->str: ...


class MemoryStorage(Storage):
    data_box = []  # атрибут класса

    def save(self, data: str) -> None:
        self.data_box.append(data)

    def load(self) -> str:
        return '\n'.join(self.data_box)




class FileStorage(Storage):
    def save(self,data:str)->None:
        with open('Newfile.txt','a',encoding='utf-8') as x:
            x.write(f'{data}\n')

    def load(self)->str:
        try:
            with open('Newfile.txt','r',encoding='utf-8')as x:
                return x.read()
        except FileNotFoundError:
            return ''



def useStorage(stor:Storage,data:str)->str:
    stor.save(data)
    return stor.load()

memory = MemoryStorage()
readnow = FileStorage()
for i in range(2):
    x = input('Введите строку: ')

    result = useStorage(memory,x)

print(memory.load())
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._lenght = 0

    def append(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else :
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self._lenght += 1

    def get(self,index):
        if index < 0 or index >= self._lenght:
            raise IndexError(f"Индекс {index} вне диапазона списка (0-{self._length - 1})")
        current = self.head
        current_index = 0
        while current_index < index:
            current = current.next
            current_index += 1
        return current.data

    def remove(self,index):
        if index < 0 or index >= self._lenght:
            raise IndexError(f"Индекс {index} вне диапазона списка (0-{self._length - 1})")
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            current_index = 0
            while current_index < index - 1:
                current = current.next
                current_index += 1


            current.next = current.next.next
        self._lenght -= 1
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __str__(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        return '[' + ' '.join(elements) + ']'

    def __len__(self):
        return self._lenght

my_list = LinkedList()
my_list.append(40)
my_list.append(50)
my_list.append(20)

print(f'Текуший лист {my_list}')
print(f'Получения третьего элемента {my_list.get(2)}')
print('Удаления второго элемента')
my_list.remove(1)
print(f'Новый список {my_list}')

print('Итерация по списку')
for i in my_list:
    print(i)
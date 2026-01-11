

class LRUCache:
    def __init__(self,limit):
        self.limit = limit
        self.dict = dict()

    @property
    def cache(self):
        if self.dict:
            old_elem = next(iter(self.dict))
            return old_elem, self.dict[old_elem]
        return None
    @cache.setter
    def cache(self,new_elem):
        key,vallues = new_elem
        if key in self.dict:
            self.dict.pop(key)
        elif len(self.dict) >= self.limit:
            start_inf = next(iter(self.dict))
            self.dict.pop(start_inf)
        self.dict[key] = vallues

    def print_cache(self):
        for key,vallues in self.dict.items():
            print(f'{key} : {vallues}')
    def get(self,new_elem):
        if new_elem in self.dict:
            vallues = self.dict.pop(new_elem)
            self.dict[new_elem] = vallues
            return vallues
        return None

cache = LRUCache(3)

cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3","vallue3")
cache.cache = ("key4","vallue4")
cache.print_cache()
print(cache.get('key3'))
cache.print_cache()
print(cache.cache)


# cache.print_cache()
# print(cache.get("key2"))
# cache.print_cache()
# cache.cache = ("key3", "value3")
# cache.cache = ("key4", "value4")
# cache.cache = ("key5", "value5")
#
#
# cache.print_cache()
# print(cache.cache)











# Пример:
# # Создаём экземпляр класса LRU Cache с capacity = 3
# cache = LRUCache(3)
# # Добавляем элементы в кэш
# cache.cache = ("key1", "value1")
# cache.cache = ("key2", "value2")
# cache.cache = ("key3", "value3")
# # # Выводим текущий кэш
# cache.print_cache() # key1 : value1, key2 : value2, key3 : value3
# # Получаем значение по ключу
# print(cache.get("key2")) # value2
# # Добавляем новый элемент, превышающий лимит capacity
# cache.cache = ("key4", "value4")
# # Выводим обновлённый кэш
# cache.print_cache() # key2 : value2, key3 : value3, key4 : value4
# Ожидаемый вывод в консоли:
# LRU Cache:
# key1 : value1
# key2 : value2
# key3 : value3
# value2
# LRU Cache:
# key3 : value3
# key2 : value2
# key4 : value4
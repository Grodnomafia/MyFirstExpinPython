class Example:
    def __init__(self):
        print('Вызов инит')
        self.count = 0
        self.suppress_exception = False

    def __enter__(self):
        print('вызов энтер')
        self.count += 1
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('вызов Exit')
        if exc_type is not None:
            print(f'{exc_type}\n{exc_val}\n{exc_tb}')
            if self.count > 1:
                self.suppress_exception = True
        self.count -= 1
        if self.count == 0 and exc_type is not None and self.suppress_exception:
            return True  # подавляем исключение
        return False



my_obj = Example()
with my_obj as obj:
    print('Код внутри первого вызова контекст менеджера')
    with my_obj as obj2:
        raise Exception('Выброс исключения во вложенном (втором) вызове контекст менеджере')
    print('Я обязательно выведусь...')
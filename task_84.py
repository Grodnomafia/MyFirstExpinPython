class Date:
    def __init__(self,day,mounth,age):
        self.day = day
        self.mounth = mounth
        self.age = age

    def __str__(self):
        return f'Год: {self.age}, Месяц: {self.mounth}, День: {self.day}'
    @classmethod
    def is_date_valid(cls,text:str)->bool:
        try:
            if not text:
                return False
            day,mounth,age = text.split('-')
            day,mounth,age = int(day),int(mounth),int(age)
            if mounth < 1 or mounth > 12:
                return False
            if age < 1:
                return False
            mounth_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if day < 1 or day > mounth_day[mounth-1]:
                return False
            return True
        except Exception as e:
            print(e)
            return False
    @classmethod
    def from_string(cls,text:str):
        if cls.is_date_valid(text):
            day,mounth,age = text.split('-')
            return  cls(int(day),int(mounth),int(age))

        else:
            raise ValueError('Ошибка')






try:
    date = Date.from_string('44-12-2077')
    print(date)
except Exception as x:
    print(x)
print(Date.is_date_valid('10-!12-2077'))
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

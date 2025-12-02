import random
class KillError(Exception):
    def __str__(self):
        return f'Ошибка 1'
class DrunkError(Exception):
    def __str__(self):
        return f'Ошибка 2'
class CarCrashError(Exception):
    def __str__(self):
        return f'Ошибка 3'
class GluttonyError(Exception):
    def __str__(self):
        return f'Ошибка 4'
class DepressionError(Exception):
    def __str__(self):
        return f'Ошибка 5'



class Budism:
    KARMA_FINISH = 500
    def __init__(self):
        self.my_karma = 0
        self.day = 0


    def one_day(self):
        return random.randint(1,7)

    # def crash_error(self):
    #  if random.randint(1, 10) == 1:
    #     errors_choice = random.choice((KillError,DrunkError,CarCrashError,GluttonyError,DepressionError))
    #     return errors_choice

    def life(self):
            self.day += 1
            self.my_karma += self.one_day()



    def __str__(self):
        return f'{self.my_karma} карма , day: {self.day}'

my_karma = Budism()

with open('my_fail.txt', 'w' , encoding='utf-8') as my_fail:

        while Budism.KARMA_FINISH > my_karma.my_karma:
            try:
                my_karma.life()
                if random.randint(1,10 ) == 1:
                    errors_choice = random.choice((KillError,DrunkError,CarCrashError,GluttonyError,DepressionError))
                    raise errors_choice

            except (KillError,DrunkError,CarCrashError,GluttonyError,DepressionError) as x:
                my_fail.write(f'{str(x)}\n')
print(my_karma)







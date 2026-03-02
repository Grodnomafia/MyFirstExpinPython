class Blablabla(Exception):
    pass


def coroutine(func):
    def inner(*args,**kwargs):
        result = func(*args,**kwargs)
        result.send(None)
        return result
    return inner




def subgen():
    x = 'готов принять сообщения'
    message = yield x
    print('otvet',message)

@coroutine
def average():
    count = 0
    sum = 0
    average = None


    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
            break
        except Blablabla:
            print('fafafafaf')
            break
        else:
            count += 1
            sum += x
            average = round(sum / count,2)
    return average
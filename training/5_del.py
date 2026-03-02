
def coroutine(func):
    def inner(*args,**kwargs):
        result = func(*args,**kwargs)
        result.send(None)
        return result
    return inner

class Blablabla(Exception):
    pass

def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            break
        else:
            print('......',message)
    return 'Возрошает сабген'
@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except Blablabla as e:
    #         g.throw(e)
    result = yield from g
    print(result)




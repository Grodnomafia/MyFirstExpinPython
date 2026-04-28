import asyncio
import random


async def unstable():
    await asyncio.sleep(0.2)
    if random.random() < 0.5:
        raise ValueError('ошибка')
    return 'Ок'


async def run_with_retry(func, quant):
    for i in range(1, quant + 1):
        task = asyncio.create_task(func())

        try:
            result = await task
            print(f'попытка {i}: успех {result}')
            return result
        except Exception as x:
            print(f'ошибка попытки {i} ошибка {x}')
            if quant == i:
                print('Все попытки исчерпаны')
                return f'Errors'
            await asyncio.sleep(0.5)


async def main():
    result = await run_with_retry(unstable, 2)
    print('Итог', result)


asyncio.run(main())
# 1.Создайте функцию calculate(x, delay),
# которая ждёт delay секунд и возвращает квадрат числа x.
# Запустите три вызова параллельно для чисел 2, 3, 4 с задержками 1, 2, 1
# секунда соответственно. Выведите все результаты.

# import asyncio
# async def calculate(x, delay):
#     await asyncio.sleep(delay)
#     return x ** 2
# async def main():
#     result = await asyncio.gather(
#         calculate(2, 1),
#         calculate(3, 2),
#         calculate(4, 1),
#     )
#     print(result)
# asyncio.run(main())


# 2.Создайте функцию long_task(),
# которая ждёт 5 секунд.
# Запустите её как задачу, подождите 2 секунды и отмените задачу. Выведите сообщение об отмене.

# import asyncio
# async def long_task():
#     await asyncio.sleep(5)
# async def main():
#     task = asyncio.create_task(long_task())
#     await asyncio.sleep(2)
#     task.cancel()
#     print("задача отменена")
# asyncio.run(main())

# 3.Создайте функцию fetch_data(api_name, delay),
# которая возвращает строку "Данные из {api_name}".
# Запустите 4 запроса параллельно с разными задержками delay (1, 2, 1.5, 0.5 секунд) и выведите все результаты.

# import asyncio
# async def fetch_data(api_name, delay):
#     await asyncio.sleep(delay)
#     return f"Данные из {api_name}"
# async def main():
#     results = await asyncio.gather(
#         fetch_data("API_1", 1),
#         fetch_data("API_2", 2),
#         fetch_data("API_3", 1.5),
#         fetch_data("API_4", 0.5)
#     )
#     print(results)
# asyncio.run(main())


squere = lambda x: x if x == 0 else x **2
print(squere(5))

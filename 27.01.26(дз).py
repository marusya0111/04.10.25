# 1. Создайте функцию с замыканием make_stats_tracker(),
# которая возвращает четыре функции:
# для добавления числа,
# получения среднего значения, получения минимума и максимума.
# Функция должна эффективно отслеживать все необходимые статистики.

# def make_stats_tracker():
#     numbers = []
#     def number_add(num):
#         numbers.append(num)
#     def srednee_znach():
#             return sum(numbers)/len(numbers)
#     def get_mini():
#             return min(numbers)
#     def get_maxi():
#             return max(numbers)
# number_add, srednee_znach, get_mini, get_maxi = make_stats_tracker()
# number_add(10)
# number_add(20)
# number_add(30)

# 2. Создайте функцию с замыканием make_task_manager(),
# которая возвращает набор функций для управления задачами:
# добавление задачи, пометка задачи как выполненной по ID, получение списка всех задач,
# получение списка невыполненных задач и получение статистики.
# Каждая задача должна иметь уникальный ID, название и статус выполнения.

#def make_task_manager():

# 3. Напишите функцию apply_to_each(numbers, operation), которая принимает список чисел
# и функцию-колбэк, применяет эту функцию к каждому элементу списка
# и возвращает новый список с результатами.
# Протестируйте её с функциями возведения в квадрат и удвоения числа.


def apply_to_each(numbers, operation):
    return [operation(num) for num in numbers]
def kvadrat (y):
    return y**2
def udvoen (y):
    return y*2
numbers = [1,2,3,4,5]
squared = apply_to_each(numbers,kvadrat)
doubli = apply_to_each(numbers,udvoen)
print(squared, doubli)





#1 задача Даны списки.
#keys = ['name', 'age', 'city', 'profession']
#values = ['Иван', 28, 'Москва', 'Программист']
#Создайте словарь из этих списков и
# выведите его элементы с номерами строк. Используйте zip и enumerate

# keys = ['name', 'age', 'city', 'profession']
# values = ['Иван', 28, 'Москва', 'Программист']
# dictionary = dict(zip(keys, values))
# for key, values in enumerate(dictionary):
#     print(key, values)

#2 задача.Даны два списка ответов: correct_answers = ['A', 'B', 'C', 'D', 'A'] (верные)
# и student_answers = ['A', 'B', 'D', 'D', 'A']
# (ответы ученика).
# Подсчитайте количество правильных ответов среди
# ответов ученика и выведите детальную информацию.

# correct_answers = ['A', 'B', 'C', 'D', 'A']
# student_answers = ['A', 'B', 'D', 'D', 'A']
# count = 0
# for correct,student in  zip(correct_answers, student_answers):
#     if  correct == student:
#         count += 1
# print(count)

#3.Дан список списков [[2, 4, 6], [8, 10, 12], [14, 16, 18]].
# Проверьте, все ли подсписки содержат только четные числа
# a = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
# def chetnost (substring):
#     for i in substring:
#         if num %2 == 0 :
#             return True
#         return False
# result = [chetnost(sub) for lst in a]


# 4.
# Дан список температур
# [20, 22, 18, 25, 19, 21].
# Увеличьте каждую температуру на значение, равное её индексу, и выведите результат.
# temps = [20, 22, 18, 25, 19, 21]
# result = []
# for i in range(len(temps)):
#     new = temps[i]+ i
#     result.append(new)
# print(result)

#5
# Дана матрица matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]].
# Проверьте, содержит ли каждая строка хотя бы один ноль
# и есть ли ноль хотя бы в одной строке.
# Если есть, выведите индексы строк с нулями.

# matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
# row = []
# for i in range(len(matrix)):
#     if 0 in matrix[i]:
#         row.append(i)
# if row:
#     print(row)
# else:
#     ("no")






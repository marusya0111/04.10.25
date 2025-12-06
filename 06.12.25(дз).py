# 1.Создайте файл в режиме 'w' с текстом "Привет\nКак дела\n".
# Затем в режиме 'a'
# добавьте строку
# "Как погода\n"
# с помощью write().
# Прочитайте весь файл в режиме 'r' с
# помощью readlines() и выведите список строк.


# with open("test.txt", "w", encoding="utf-8") as file:
#     file.write("Привет\nКак дела\n")
#
# with open("test.txt", "a", encoding="utf-8") as file:
#     file.write("Как погода\n")
#
# with open("test.txt", "r", encoding="utf-8") as file:
#     print(file.readlines())
#
# file.close()


#2 {"A": 10, "B": 20, "C": 30}
# Замените ключи на случайные трехзначные числа.
# Запишите полученный словарь в файл в режиме 'w',
# каждую пару
# ключ-значение на новой строке
# в формате "ключ:значение\n".
# Затем прочитайте файл в режиме 'r' с помощью readlines() и выведите пары.

# import random
# x = {"A": 10, "B": 20, "C": 30}
# d = {}
# for i in x :
#     new_keys = random.randint(100,999)
#     d[i]= new_keys
# with open("test", "w", encoding="utf-8") as file:
#     for key,i in d.items():
#         file.write(f"{key} : {i}\n")
#         print(f"{key} : {i}")
# with open("test", "r", encoding="utf-8") as file:
#     print(file.readlines())

#3задание
# Создайте файл в режиме 'w' с 50 строками случайных чисел
# от 1 до 100.
# В режиме 'a' добавьте 20 строк.
# Прочитайте все в режиме 'r' с readlines() и выведите сумму всех чисел.
import random
with open("test", "w", encoding="utf-8") as file:
    for i in range (50):
        file.write()





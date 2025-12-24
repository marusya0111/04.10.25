# Через ASCI
# Реализуйте метод lower(). На вход поступает строка
# (вводится пользователем), состоящая из символов латинского алфавита
# нижнего и верхнего регистра. Необходимо вывести на экран ту
# же строку в нижнем регистре. Реализовать при помощи цикла
# for или while на ваше усмотрение.
# При необходимости можно использовать функции len(), ord(), chr().
# Входные данные:
# Hello World PyThOn
# Выходные данные:
# hello world python
# 2мя способами (разные циклы, струтуры)

def vverx (string):
    lower_str = ""
    for i in string:
        if 'A' <= i <= 'Z':
            lower_str += chr(ord(i) + 32)  # в нижний регистр
        else:
            lower_str += i #оставили такой же симводл
    return lower_str
u = input()
print(vverx(u))











# def custom_lower_while(input_string):
#     lower_string = ""
#     index = 0
#     while index < len(input_string):
#         char = input_string[index]
#         if 'A' <= char <= 'Z':  # Проверяем, является ли символ заглавной буквой
#             lower_string += chr(ord(char) + 32)  # Преобразуем в нижний регистр
#         else:
#             lower_string += char  # Оставляем символ без изменений
#         index += 1  # Переходим к следующему символу
#     return lower_string
#
# # Ввод строки от пользователя
# user_input = input("Введите строку: ")
# # Вывод результата
# print(custom_lower_while(user_input))




















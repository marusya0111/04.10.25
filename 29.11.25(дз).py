#1.
# Напишите функцию, которая принимает
# натуральное число и возвращает его факториал (используя цикл!
# def factorial(n):
#     x = 1
#     for i in range(1,n+1):
#         x = x * i
#     return x
# print(factorial(5))

# 2.
# Напишите функцию number_to_digits(n),
# которая принимает натуральное число и возвращает список его цифр.

def number_to_digits(n):
     x = []
     while n > 0:
         x = n % 10
         x.append(digit)



# 3.
# Напишите функцию is_prime(n),
# которая принимает целое число
# и возвращает True для простых чисел
# или False для чисел, не являющихся простыми.

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False



    #4
# Напишите функцию camel_to_snake(s),
# которая принимает строку
# в «верблюжьем регистре»
# (ThisIsCamelCased) и преобразует ее в «змеиный регистр» (this_is_camel_cased)

#def camel_to_snake(s):
 #   x = []
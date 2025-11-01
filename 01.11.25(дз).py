# 1. Пользователь вводит строку. Определите,
# оканчивается ли строка на "ов".
# a = input()
# print(a.endswith("ов"))
#2.Пользователь вводит строку. Определите,
#содержит ли она хотя бы одну цифру.
#b = input()
#print(b.isalpha())
#3.Разбейте строку по пробелам и соедините
#обратно через запятую.
# string = "Вышел новый сезон сериала"
# b = string.split()
# c = ",".join(b)
# print(b)
# print(c)
#4.Удалите все гласные буквы из строки.
# glasn = "аеёиоуеэыяюАЕЁИОУЫЭЮЯ"
# str = "Ёжики любят купаться"
# for i in glasn:
#     str = str.replace(i, "")
# print(str)


#16.
a = input()
alpha = ""
amount = 0
#уникализирует список [1,2,3,4]
setter = set(a)
for i in setter:
    count = a.count(i)
    if count > amount:
        alpha = i
        amount = count
print(alpha,amount)
print(a[::3])
maxim = 0
indexes = ""
for i in setter:
    if a.count(i) == 1:
        continue
    backward = a.rfind(i)
    forward = a.find(i)
    if (backward - forward) > maxim:
        maxim = backward - forward
        indexes = a[backward:forward]
print(indexes)




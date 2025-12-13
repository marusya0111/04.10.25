# Откройте файл 907, содержащий в каждой строке пять
# натуральных чисел. Определите количество строк таблицы,
# для чисел которых выполнены оба условия:
# в строке все числа различны;
# сумма двух наибольших чисел строки не больше
# суммы трёх её оставшихся чисел.


with open("907.txt","r") as file:
    counter = 0
    s = []
    for line in file:
        numbers = line.split("\t")
        for i in numbers:
            s.append(int(i))
        s = sorted(s)
        if len(set(s)) == 5 and sum(s[0]+s[1])<= sum(s[1:5]):
            counter += 1
print(counter)









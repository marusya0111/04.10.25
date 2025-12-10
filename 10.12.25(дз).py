# 1.Откройте файл 902, содержащий
# в каждой строке четыре натуральных числа.
# Определите количество строк, содержащих числа, для которых выполнены оба условия:
# наибольшее из четырёх чисел меньше суммы трёх других;
# среди четырёх чисел есть только одна пара равных чисел.

with open("902.txt","r") as f:
    count = 0
    for line in f:
        numbers = line.split("\t")
        sorted_numbers = sorted(numbers)
        maxim = sorted_numbers[3]
        summa = sum(sorted_numbers[:3])
        if summa > maxim:
            count+=1
        print(count)
# 2.Откройте файл 903, содержащий в каждой
# строке четыре натуральных числа.
# Определите количество строк, в которых сумма
# наибольшего и
# наименьшего чисел не больше суммы двух оставшихся.
with open("903.txt","r") as f:
    count = 0
    for line in f:
        numbers = line.split("\t")
        sorted_numbers = sorted(numbers)
        maxim = sorted_numbers[3]
        mini = sorted_numbers[0]
        sum_min_maxim = mini + maxim
        another_numbers = sorted_numbers[0:3]
        summa_another_numbers = sum(another_numbers)
        if sum_min_maxim < summa_another_numbers:
            count = count + 1
            print(count)





















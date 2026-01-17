# 1. Откройте файл 914.txt содержащий в каждой строке семь натуральных чисел.
#
# Определите сумму чисел в строке с наибольшим номером, для которой выполнены оба условия:
# — в строке есть одно число, которое повторяется трижды, остальные четыре числа различны;
# — среднее арифметическое неповторяющихся чисел строки не больше повторяющегося числа.

# with open("914.txt") as f:
#     data = [list(map(int, i.split())) for i in f]
#
# def f1(line):
#     cnt_3 = [i for i in line if line.count(i) == 3]
#     cnt_1 = [i for i in line if line.count(i) == 1]
#     return len(cnt_3)== 3 and len(cnt_1)== 4
#
# def f2(line):
#     rep = [i for i in line if line.count(i) != 1]
#     norep = [i for i in line if line.count(i) == 1]
#     aver = sum(norep)/len(norep)
#     return aver < rep[0]
#
# for pos,val in list(enumerate(data,start = 1))[::-1]:
#     if f1(val) and f2(val):
#         print(pos)
#         break

# 2.Откройте файл 907.txt, содержащий в каждой строке пять натуральных чисел.
# Определите количество строк таблицы, для чисел которых выполнены оба условия:
# – в строке все числа различны;
# – сумма двух наибольших чисел строки не больше суммы трёх её оставшихся чисел.

with open("907.txt") as f:
    data = [list(map(int, i.split())) for i in f]
def f1(line):
    return len(line) == len(set(line))
def f2(line):
    line.sort()
    sum_max = line[-1] + line[-2]
    sum_other_numbers = sum(line[0:-2])
    return sum_max < sum_other_numbers
count = 0
for line in data:
    if f1(line) and f2(line):
        count += 1
print(count)















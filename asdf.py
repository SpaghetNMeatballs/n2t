row_max = []
column_max = []

l = int(input('Введите количество строк в матрице:\n'))
print('Введите матрицу построчно:')
for i in range(l):
    p = [int(i) for i in input().split()]
    row_max.append(max(p))
    if i == 0:
        column_max = p
    else:
        for q in range(len(column_max)):
            if column_max[q] < p[q]:
                column_max[q] = p[q]

'''for i in range(len(b)):
    row_max.append(max(b[i]))

for i in range(len(b[0])):
    maximum = b[0][i]
    for q in range(len(b)):
        if b[q][i] > maximum:
            maximum = b[q][i]
    column_max.append(maximum)'''

for k in range(int(input('Введите количество замен:\n', ))):
    row, column, value = [int(i) for i in
                          input(
                              'Введите замену в формате "Номер_строки_сверху_вниз Номер_числа Значение_замены":\n').split()]
    if row_max[row - 1] < value:
        row_max[row - 1] = value
    if column_max[column - 1] < value:
        column_max[column - 1] = value
    cntr = 0
    """
    for x in range(len(column_max)):
        for y in range(len(row_max)):
            if column_max[x] == row_max[y]:
                cntr += 1"""
    if len(column_max) < len(row_max):
        for x in column_max:
            if x in row_max:
                cntr += 1
    else:
        for x in row_max:
            if x in column_max:
                cntr += 1
    print(cntr)

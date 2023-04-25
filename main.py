from typing import List


def maxElem(array, inelem):
    summ = 0
    for i in range(len(array)):
        if i != inelem:
            summ += abs(array[i])
    return abs(array[inelem]) > summ

def diagonal_dominant(matrix, matrix_b):
    print("Проверка на возможность достижения диагонального преобладания")
    n = len(matrix)
    inarray = []
    for i in range(n):
        for j in range(n):
            if maxElem(matrix[i], j):
                if j in inarray:
                    raise Exception("Невозможно достичь диагональное преобладание")
                inarray.append(j)
    if len(inarray) == n:
        a = [[0 for j in range(n)] for i in range(n)]
        b = [0] * n
        for i in range(len(matrix)):
            a[inarray[i]] = matrix[i]
            b[inarray[i]] = matrix_b[i]
        print("Достигнуто диагональное преобладание")
        return a, b
    raise Exception("Невозможно достичь диагональное преобладание")


def EnterE():
    try:
        e = float(input("Ведите точность = ").replace(",", "."))
    except Exception:
        print("Некорректный ввод, попробуйте ещё раз")
        return EnterE()
    return e


def EnterN():
    try:
        n = int(input("Введите размерность матрицы = "))
    except Exception:
        print("Некорректный ввод, попробуйте ещё раз")
        return EnterN()
    if n > 20 or n < 3:
        print("Недопустимое значение, попробуйте ещё раз")
        return EnterN()
    return n


def EnterZ():
    try:
        z = float(input("Ведите значение = ").replace(",", "."))
    except Exception:
        print("Некорректный ввод, попробуйте ещё раз")
        return EnterZ()
    return z


a = []
b = []
way = ""
while way not in ["+", "-"]:
    print('Введите "+" если хотите начать ввод с клавиатуры, или введите "-" если хотите вводить из файла')
    way = input()
if way == "+":
    E = EnterE()
    n = EnterN()
    a = []
    b = [0] * n
    print("Введите значения матрицы A:")
    for i in range(n):
        a.append([])
        for j in range(n):
            a[i].append(EnterZ())
            # a[i][j] = EnterZ()
    print("Введите значения вектора B:")
    for i in range(n):
        b[i] = EnterZ()
    print("Ввод с клавиатуры окончен, все данные введены корректно")
else:
    # f = open('input.txt', 'r')
    # l = []
    # l = [line.split() for line in f]
    # print
    # l
    e = 0
    print("Ввод из файл окончен, все данные введены корректно")
try:
    A, B = diagonal_dominant(a, b)
    n = len(A)
    x = [float(0)] * n
    table = [[]]

    flag = True
    limit = 500
    k = 0

    while flag and k < limit:
        table.append([])
        temp = x.copy()
        for i in range(n):
            summ = 0
            for j in range(n):
                if j == i:
                    continue
                summ += A[i][j] * temp[j]
            x[i] = (B[i] - summ) / A[i][i]
            table[k].append(x[i])

        top = float(0)
        for i in range(n):
            e = abs(x[i] - temp[i])
            table[k].append(e)
            if e > top:
                top = e

        if top < E:
            flag = False

        k += 1
    for i in table:
        for j in i:
            print(j, end=' ')
        print('')
except Exception as ex:
    print(str(ex))




# A = [
#     [1.7, 3.8, 1.9],
#     [4.1, 1.4, 1.8],
#     [2.2, -1.7, 4.3]]
# B = [0.7, 1.1, 2.8]


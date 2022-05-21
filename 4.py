import random

print("Предположим подматрица С:")
len = 10 # Длина подматрицы
A = [[0]*len for row in range(len)]
for row in range(len):
    for column in range(len):
        A[row][column] = random.randint(-10, 10)
        print("{:4}".format(A[row][column]), end=" ")
    print()

# Алгоритм по подсчету минимума
min = A[0][0] # Сначала за минимум берем первое число
cout_min = 0 # Счетчик минимальных значений
for row in range(len):
    for column in range(0, len, 2): # Идем с шагом два, так как нам нужны только нечетные столбцы
        if min > A[row][column]: # Если находим новый минимум то:
            min = A[row][column]
            cout_min = 1 # Обновляем счетчик
        elif min == A[row][column]:
            cout_min += 1
print(cout_min)

# Алгоритм по подсчету максимума
max = A[0][0] # Сначала за максимум берем первое число
cout_max = 0 # Счетчик максимальных значений
for row in range(0, len, 2): # Идем с шагом два, так как нам нужны только нечетные строки
    for column in range(len):
        if max < A[row][column]: # Если находим новый максимум то:
            max = A[row][column]
            cout_max = 1 # Обновляем счетчик
        elif max == A[row][column]:
            cout_max += 1
print(cout_max)
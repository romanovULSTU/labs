"""10.Формируется матрица F следующим образом: скопировать в нее А и если в С количество минимальных чисел
в нечетных столбцах больше, чем количество максимальных чисел в четных строках, то поменять местами В и С симметрично,
иначе С и Е поменять местами несимметрично. При этом матрица А не меняется.
После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,
то вычисляется выражение: A-1*A – K * F, иначе вычисляется выражение (AТ +GТ-F-1)*K, где G-нижняя треугольная матрица, полученная из А.
Выводятся по мере формирования А, F и все матричные операции последовательно."""

import time
import numpy as np

print("\n-----Результат работы программы-------")
try:
    N = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100: "))
    while N < 6 or 100 < N:
        N = int(input("Введите количество строк (столбцов) квадратной матрицы в интервале от 6 до 100: "))

    K = int(input("Введите число К: "))
    start = time.time()
    A = np.random.randint(-10, 10, (N, N))  # заполняем матрицу А
    print("Матрица А:")
    print(A)
    F = A.copy()                        # копируем матрицу А в матрицу F
    print("Матрица F:")
    print(F)
    n = N // 2                          # размер подматрицы С
    C = np.zeros((n, n))                # заполняем подматрицу C нулями
    print("Матрица C:")
    print(C)

    for i in range(n):                  # заполняем подматрицу C элементами из матрицы F
        for j in range(n):
            C[i][j] = F[i][n + (N % 2) + j]
    print("Матрица C")
    print(C)

    min = C[0][0]  # Сначала за минимум берем первое число
    cout_min = 0
    for i in range(n):
        for j in range(0, n, 2):  # Идем с шагом два
            if min > C[i][j]:  # Если находим новый минимум то:
                min = C[i][j]
                cout_min = 1  # Обновляем счетчик
            elif min == C[i][j]:
                cout_min += 1
    max = C[0][0]  # Сначала за максимум берем первое число
    cout_max = 0
    for i in range(0, n - 1, 2):  # Идем с шагом два
        for j in range(n - 1):
            if max < C[i][j]:  # Если находим новый максимум то:
                max = C[i][j]
                cout_max = 1  # Обновляем счетчик
            elif max == C[i][j]:
                cout_max += 1
    print(cout_min,cout_max)

    if cout_min > cout_max:
        for i in range(n):
            for j in range(n + N % 2,1):
                F[i][j], F[i][j + n + N % 2] = F[i][j + n + N % 2], F[i][j] # BC simm
    else:
       for j in range(n):
            for i in range(n):
                F[i][j], F[i][n + N % 2 + j] = F[i][n + N % 2 + j], F[i][j] # CE nesimm
    print("Матрица F")
    print(F)

    if np.linalg.det(A) == 0 or np.linalg.det(F) == 0:  # если один из определителей = 0
        print("Нельзя вычислить")
    elif np.linalg.det(A) > np.trace(F):
        result = ((A.dot(np.linalg.inv(A))) - (K * F))  # A-1*A – K * F
    else:
        result = (np.transpose(A) + np.transpose(np.tril(A)) - (np.linalg.inv(F))) * K  # (AТ +GТ-F-1)*K

    print("\nРезультат вычисления выражения:")
    for i in result:
        for j in i:
            print("%5d" % j, end=' ')
        print()

    finish = time.time() - start
    print("\n", "Program time: " + str(finish) + " seconds.")

except ValueError:
    print("\nэто не число")
except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.")

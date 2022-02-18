def insertion_sort(list):
    for i in range(1, len(list)):
        n = list[i]
        j = i - 1
        while (j >= 0 and list[j] > n):
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = n
r_list=[5324,12863,346273,234,654,26,875,44234,86780,3545,13,4,556,34552,4692]
print('Исходный список: ',r_list)
insertion_sort(r_list)
print('Отсортированный список: ',end='')
print(r_list)

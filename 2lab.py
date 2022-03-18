"""Вариант 10. Написать программу, которая читая последовательность
чисел из файла, выводит на экран все числа, меняя порядок цифр в них на обратный."""

import os
import time

more_max_buffer_len = False  
max_buffer_len = 200    # максимальный размер рабочего буфера

buffer_len = 1          # размер буфера чтения
work_buffer = ""        # рабочий буфер


try:
    print("\nxXx--Результат работы программы--xXx\nxXx--Локальное время",time.ctime(),"--xXx\n")
    start = time.time()       
    with open("input.txt", "r") as file:   # открываем файл
        line = file.read(buffer_len)          
        if not line:                        # если файл пустой
            print ("\nФайл input.txt в директории проекта пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
        for line in file:                   # пока есть строки   
            if line:   
                work_buffer += '*'
                if len(work_buffer) >= max_buffer_len :    # Если буфер переполнен
                    print ("\nФайл input.txt содержит блок цифр, превышающий максимальный размер буфера = "+str(max_buffer_len) + " строк.\nОткорректируйте файл text.txt в директории или переименуйте существующий *.txt файл.")
                    more_max_buffer_len = True
                    if more_max_buffer_len:
                        break               #выход из цикла
                else:
                    line = line.strip()[::-1]       #переворачиваем числа
                    print(line)                     #выводим нужные числа
            
        finish = time.time()        
        result = finish - start                 #время выполнения
        print("Program time: " + str(result) + " seconds.")
        
except FileNotFoundError:
    print("\nФайл input.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.") 
    


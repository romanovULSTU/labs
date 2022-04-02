"""Вариант 10. Написать программу, которая читая последовательность
чисел из файла, выводит на экран все числа, меняя порядок цифр в них на обратный."""

import os
import time

more_max_buffer_len = False  
max_buffer_len = 100    # максимальный размер рабочего буфера
buffer_len = 1          # размер буфера чтения
work_buffer = ""        # рабочий буфер
number_flag = False


try:
    print("\nxXx--Результат работы программы--xXx\nxXx--Локальное время",time.ctime(),"--xXx\n")
    start = time.time()       
    with open("input.txt", "r") as file:        # открываем файл
        buffer = file.read(buffer_len)          # читаем первую строку
        if not buffer:                          # если файл пустой
            print ("\nФайл input.txt в директории проекта пустой.\nДобавьте не пустой файл в директорию или переименуйте существующий *.txt файл.")
        while buffer:                           # пока файл не пустой
            while (buffer<'0' or buffer>'9') and buffer:        # ищем цифры
                buffer = file.read(buffer_len)                  # продолжаем читать
            while (buffer >= '0' and buffer <= '9') and buffer:     
                number_flag= True                           # наличие цифр
                work_buffer += buffer                       
                if len(work_buffer) >= max_buffer_len :     # Если буфер переполнен
                    print ("\nФайл input.txt содержит блок цифр, превышающий максимальный размер буфера = "+str(max_buffer_len) + " строк.\nОткорректируйте файл input.txt в директории или переименуйте существующий *.txt файл.")
                    more_max_buffer_len = True
                buffer = file.read(buffer_len)              # читаем следующий блок
            if more_max_buffer_len:             # выходим из цикла если буффер переполнен
                    break
            if number_flag == True:
                print(work_buffer.strip()[::-1],'\n')       # печатем число
            if not number_flag and not buffer and len(work_buffer) >0:
                print("\n Файл input.txt не содержит ни одной цифры.")
                break

                
            work_buffer = ""        #обновляем переменные
            number_flag = False          

            
        finish = time.time()        # останавливаем время
        result = finish - start
        print("Program time: " + str(result) + " seconds.")
except FileNotFoundError:
    print("\nФайл input.txt в директории проекта не обнаружен.\nДобавьте файл в директорию или переименуйте существующий *.txt файл.") 

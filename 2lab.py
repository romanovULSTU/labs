data = open ("input.txt",'r')   #открываем файл                 
while True:
    line = data.readline()                                                                                 
    if not line:                #выходим из цикла , если строка пустая     
        break                    
    print(line.strip()[::-1])   #выводим переворот срезом

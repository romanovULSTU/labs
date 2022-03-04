data = open ("input_for_2lab.txt")
n_list = list(data)
print('Числа с  обратным порядком цифр:\n')
for n in n_list:
    n = int(n)
    if n >10000:
        print(n%10,(n//10)%10,(n//100)%10,(n//1000)%10,(n//10000)%10,sep='')
    elif 1000< n <10000:
        print(n%10,(n//10)%10,(n//100)%10,(n//1000)%10,sep='')
    elif 100< n <1000:
        print(n%10,(n//10)%10,(n//100)%10,sep='')
    elif  10< n <100:
        print(n%10,(n//10)%10,sep='')
    else:
        print(n)
        


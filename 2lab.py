import cProfile, pstats  ,io    #4052 function calls in 0.091 seconds
from pstats import SortKey               
pr = cProfile.Profile()                         
pr.enable()

 
data = open ("input.txt",'r')   #открываем файл                 
while True:
    line = data.readline()                                                                                 
    if not line:                #выходим из цикла , если строка пустая     
        break                    
    print(line.strip()[::-1])   #выводим переворот срезом

    
pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())


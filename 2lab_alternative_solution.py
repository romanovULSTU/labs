import cProfile, pstats, io     #4014 function calls in 0.107 seconds
from pstats import SortKey
pr = cProfile.Profile()
pr.enable()


with open("input.txt") as f:
    for line in f:
        line = line.strip()[::-1]
        print(line)

        
pr.disable()
s = io.StringIO()
sortby = SortKey.CUMULATIVE
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())

with open("input.txt") as f:         #4014 function calls in 0.107 seconds
    for line in f:
        line = line.strip()[::-1]
        print(line)

t = int(input())

for _ in range(t):
    n = int(input())
    
    total = 0
    for _ in range(1, n + 1):
        if _ % 2 != 0:
            total += (n + (1 - _)) ** 2
    print(total)
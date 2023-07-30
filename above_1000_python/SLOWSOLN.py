t = int(input())

for _ in range(t):
    maxT, maxN, sumN = map(int, input().split())
    
    total_n = 0
    total_i = 0
    for _ in range(maxT):
        if total_n < sumN:
            val = min(maxN, sumN - total_n)
            total_n += val
            total_i += pow(val, 2)
    print(total_i)        
        
for _ in range(int(input())):
    n = int(input())
    
    speeds = list(map(int, input().split()))
    
    i = 1
    total = 1
    slowest = speeds[0]
    while i < n:
        if n == 1:
            break
        else:
            slowest = min(slowest, speeds[i])
            if speeds[i] <= slowest:
                total += 1
        i += 1
    print(total)
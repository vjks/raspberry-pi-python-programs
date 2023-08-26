for _ in range(int(input())):
    n, p, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    
    time = 0
    for _ in range(p):
        if a[_] == 0:
            time += x
        else:
            time += y
    print(time)
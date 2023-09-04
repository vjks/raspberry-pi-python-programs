t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    d = dict()
    for flavor in a:
        if flavor not in d:
            d[flavor] = 1
        else:
            d[flavor] += 1
    
    value = 0
    total_keys = 0
    for key in d:
        total_keys += 1

    if n == x:
        print(0)
    elif n > x:
        print(min(n - x, total_keys))
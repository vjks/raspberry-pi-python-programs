t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    points = 0
    d = dict()
    
    for _ in range(n):
        if a[_] in d:
            d[a[_]] += 1
        else:
            d[a[_]] = 1
    
    for key, value in d.items():
        if key == 2:
            points += 1
        else:
            points += min(value, key - 1)

    print(points)
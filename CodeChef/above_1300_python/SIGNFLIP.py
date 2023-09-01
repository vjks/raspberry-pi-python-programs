t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    a.sort()
    
    for _ in range(k):
        if a[_] < 0:
            a[_] = a[_] * (-1)
    
    a.sort()
    
    total = 0
    for _ in a:
        if _ > 0:
            total += _
    
    print(total)
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    a = list(map(int, input().split()))
    
    d = dict()
    dis = list()
    for _ in range(n):
        if a[_] != _ + 1:
            if a[_] in d:
                d[a[_]] += 1
            else:
                d[a[_]] = 1
        else:
            dis.append(a[_])
    count = 0
    for key, value in d.items():
        if key not in dis and value >= k:
            count += 1
    print(count)
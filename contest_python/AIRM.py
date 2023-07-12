t = int(input())

for _ in range(t):
    n = int(input())
    arrival = list(map(int, input().split()))
    departure = list(map(int, input().split()))
    
    d = dict()
    for x in arrival:
        if x not in d:
            d[x] = 1
        else:
            d[x] = d[x] + 1
    
    for y in departure:
        if y not in d:
            d[y] = 1
        else:
            d[y] = d[y] + 1
    
    print(max(d.values()))
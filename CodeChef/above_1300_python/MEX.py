t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    
    d = dict()
    
    for x in s:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    
    i = 0
    while k > 0:
        if i not in d:
            d[i] = 1
            k -= 1
        i += 1
    
    high = max(d)
    i = 0
    key_found = False
    while i < high:
        if i not in d.keys():
            key_found = True
            print(i)
            break
        i += 1
    
    if not key_found:
        print(high + 1)
    
    
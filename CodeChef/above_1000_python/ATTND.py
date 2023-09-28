def printName(name, d):
    if name[0] in d and d[name[0]] > 1:
        print(name[0], name[1])
    else:
        print(name[0])

t = int(input())

for _ in range(t):
    n = int(input())
    
    d = dict()
    names = list()
    for _ in range(n):
        first, last = map(str, input().split())
        names.append((first, last))
        
        if first in d:
            d[first] += 1
        else:
            d[first] = 1
            
    for name in names:
        printName(name, d)
        
t = int(input())

for _ in range(t):
    n = int(input())
    
    h = 0
    
    while n > 0:
        h += 1
        n -= h

    if n < 0:   
        print(h - 1)
    else:
        print(h)
t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    s = input()
    
    if x < y:
        if s.count("01") > 0 or s.count("10") > 0:
            print(x)
        else:
            print(0)
    elif y < x: 
        if s.count("10") > 0 or s.count("01") > 0:
            print(y)
        else:
            print(0)
    elif x == y:
        if s.count("01") > 0 or s.count("10") > 0:
            print(x)
        else:
            print(0)
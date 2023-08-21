t = int(input())

for _ in range(t):
    x, y, z = map(int, input().split())
    
    possible = False
    b = x
    a = y * z
    if a % b == 0:
        print(a, b)
        possible = True
    
    if possible == False:
        b = y
        a = x * z
        if a % b == 0:
            print(a, b)
            possible = True
    
    if possible == False:
        b = z
        a = x * y
        if a % b == 0:
            print(a, b)
            possible = True
    
    if possible == False:
        print(-1)
for _ in range(int(input())):
    n, a, b, c = map(int, input().split())
    
    dish1 = min(a, b)
    dish2 = min(b - dish1, c)
    
    if n <= dish1 + dish2:
        print("YES")
    else:
        print("NO")
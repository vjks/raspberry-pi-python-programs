t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    
    if n % x == 0: 
        print("YES")
    elif (n - x) % 2 == 1 and x % 2 == 0:
        print("NO")
    else:
        print("YES")
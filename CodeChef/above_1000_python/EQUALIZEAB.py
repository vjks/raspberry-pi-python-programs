t = int(input())

for _ in range(t):
    a, b, x = map(int, input().split())
    
    if (a - b) % (2 * x) == 0:
        print("YES")
    else:
        print("NO")
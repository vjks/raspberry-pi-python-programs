t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    mx = 0
    count = 0
    for x in a:
        mx = max(mx, x)
        if mx == x:
            count += 1
    print(n - count)
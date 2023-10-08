t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    
    if n == 1:
        print(0)
    else:
        horizontal = n - 1
        vertical = n - 1
        diag_1 = min(x - 1, y - 1)
        diag_2 = min(x - 1, n - y)
        diag_3 = min(y - 1, n - x)
        diag_4 = min(n - x, n - y)
        print(horizontal + vertical + diag_1 + diag_2 + diag_3 + diag_4)
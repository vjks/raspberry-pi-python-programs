t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    if n < k:
        print(n)
    else:
        if k == 0:
            print(n)
        else:
            dividend = n // k
            print(n - dividend * k)
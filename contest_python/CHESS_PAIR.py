t = int(input())

for _ in range(t):
    n, x = map(int, input().split())

    if x == 0 or n >= x:
        print(0)
    elif x > n:
        print((x - n) * 2)
        
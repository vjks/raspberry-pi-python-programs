t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    a = a[min(n - 1, k):]
    print(a[0])
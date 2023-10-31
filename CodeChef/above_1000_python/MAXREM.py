n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

max = 0
for _ in range(1, n):
    if _ == n - 1:
        print(0)
    elif a[0] != a[_]:
        print(a[_] % a[0])
        break
    else:
        continue
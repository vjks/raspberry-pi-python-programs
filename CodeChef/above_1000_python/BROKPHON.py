t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = set()
    for _ in range(n - 1):
        if a[_] != a[_ + 1]:
            b.add(_)
            b.add(_ + 1)
    print(len(b))
            
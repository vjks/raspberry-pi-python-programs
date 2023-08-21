t = int(input())

for _ in range(t):
    n, p, x, y = map(int, input().split())
    array = list(map(int, input().split()))
    time = 0
    for _ in range(p):
        if array[_] == 1:
            time += y
        elif array[_] == 0:
            time += x
    print(time)
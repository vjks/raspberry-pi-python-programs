tests = int(input())

for _ in range(tests):
    n, k = map(int, input().split())
    values = map(int, input().split())
    count = 0
    for value in values:
        if (value + k) % 7 == 0:
            count += 1
    print(count)
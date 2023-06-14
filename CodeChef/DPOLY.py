tests = int(input())

for _ in range(tests):
    n = int(input())
    list_coefficient = list(map(int, input().split()))
    degree = 0

    for y in reversed(range(n)):
        if(list_coefficient[y] != 0):
            degree = y
            break
    print(degree)
tests = int(input())

for _ in range(tests):
    number = int(input())
    sum = 1
    for x in range(number):
        sum = sum * (x + 1)
    print(sum)
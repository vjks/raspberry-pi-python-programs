tests = int(input())

for _ in range(tests):
    num_women = int(input())
    ages = list(input().split())
    count = 0
    for _ in ages:
        if int(_) >= 10 and int(_) <= 60:
            count += 1
    print(count)
weeks = list(map(int, input().split()))

count = 0

for week in weeks:
    if week >= 10:
        count += 1

print(count)
n, m, k = map(int, input().split())
i = 0
count = 0
while(i < n):
    times_questions = list(map(int, input().split()))
    sum = 0
    for _ in range(k):
        sum += times_questions[_]
    if sum >= m and times_questions[k] <= 10:
        count += 1
    i += 1
print(count)
        
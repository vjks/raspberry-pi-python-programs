n, d = map(int, input().split())

lengths = []
for _ in range(n):
    lengths.append(int(input()))

lengths.sort()

count = 0
i = 0
while(i < n - 1):
    if abs(lengths[i] - lengths[i + 1]) <= d:
        count += 1
        i += 2
    else:
        i += 1
print(count)
    
    
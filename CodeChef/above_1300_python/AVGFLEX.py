t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    count = 0
    for i in range(n):
        less = 0
        greater = 0
        for j in range(n):
            if a[j] <= a[i]:
                less += 1
            elif a[j] > a[i]:
                greater += 1
        if less > greater:
            count += 1
    print(count)
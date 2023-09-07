t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    k = int(input())
    
    count = 0
    
    for difficulty in reversed(a):
        if difficulty <= k:
            k -= difficulty
            count += 1
        else:
            break
    print(10 - count)
            
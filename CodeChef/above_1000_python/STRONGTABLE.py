t = int(input())


for _ in range(t):
    n = int(input())
    weight = list(map(int, input().split()))
    weight.sort(reverse = True)
    
    total = 0
    for _ in range(1, n + 1):
        total = max(total, weight[_ - 1] * _)
    print(total)
        
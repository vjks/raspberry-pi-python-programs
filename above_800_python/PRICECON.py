t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    prices = list(map(int, input().split()))
    loss = 0
    for p in prices:
        if p > k:
            loss += p - k
    print(loss)
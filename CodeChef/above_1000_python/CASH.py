t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    coins = list(map(int, input().split()))

    total = 0    
    for coin in coins:
        total += coin
    print(total % k)
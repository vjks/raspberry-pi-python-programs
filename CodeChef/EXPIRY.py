tests = int(input())

for x in range(tests):
    loaves, expiry, can_eat = map(int, input().split())
    leftover_loaves = expiry * can_eat
    if loaves <= leftover_loaves:
        print("YES")
    else:
        print("NO")
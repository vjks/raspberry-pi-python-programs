T = int(input())

for x in range(T):
    capacity, willing, cost = map(int, input().split())
    if willing > (capacity * 10):
        print(capacity * 10 * cost)
    else:
        print(cost * willing)
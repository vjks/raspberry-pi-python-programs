t = int(input())

for _ in range(t):
    items = list(map(int, input().split()))
    
    x = items.pop(0)
    
    items.sort()
    
    cheapest = items[0]
    cheapest2 = items[1]
    
    total = cheapest2 + cheapest * (x - 1)
    print(total)
    
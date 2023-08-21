t = int(input())

for _ in range(t):
    s, a, b, c = map(int, input().split())
    
    change = s * (c / 100)
    
    if c < 0:
        change = -abs(change)
    
    price = s + change
    if price >= a and price <= b:
        print("YES")
    else:
        print("NO")
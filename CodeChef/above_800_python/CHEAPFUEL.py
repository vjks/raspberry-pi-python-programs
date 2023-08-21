T = int(input())

for _ in range(T):
    x, y, a, b, k = map(int, input().split())
    
    petrol = x + (a * k)
    diesel = y + (b * k)
    
    if petrol < diesel:
        print("PETROL")
    elif diesel < petrol:
        print("DIESEL")
    else:
        print("SAME PRICE")
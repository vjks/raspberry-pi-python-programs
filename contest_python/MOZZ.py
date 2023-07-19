import math
t = int(input())

for _ in range(t):
    x, y, r = map(int, input().split())
    thirties = r / 30
    plates = 0
    
    total = x + thirties
    plates = math.ceil(total / y)
    print(plates)
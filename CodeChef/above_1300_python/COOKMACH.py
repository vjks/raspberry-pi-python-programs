t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    
    count = 0
    while b % a != 0:
        a = int(a / 2)    
        count += 1
        
    while b != a:
        a *= 2
        count += 1
    print(count)
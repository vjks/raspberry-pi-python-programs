import math

t = int(input())

for _ in range(t):
    n, a, b, k = map(int, input().split())
    
    lcm = math.lcm(a, b)
    by_lcm = n // lcm 
    by_a = n // a
    by_b = n // b
    
    if by_a + by_b - (2 * by_lcm) >= k:
        print("Win")
    else:
        print("Lose")
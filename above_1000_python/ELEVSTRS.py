import math

t = int(input())

for _ in range(t):
    n, v1, v2 = map(int, input().split())
    
    t_elevator = 2 * (n / v2)
    t_stairs = (n * math.sqrt(2)) / v1
    
    if t_elevator < t_stairs:
        print("Elevator")
    else:
        print("Stairs")
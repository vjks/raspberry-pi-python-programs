import math

t = int(input())

for _ in range(t):
    h, x, y1, y2, k = map(int, input().split())
    
    x_damage = math.ceil(h / x)
    if y1 * k >= h:
        y_damage = math.ceil(h / y1);
    else:
        h = h - (y1 * k);
        y_damage = math.ceil(h / y2) + k
    print(min(x_damage, y_damage))
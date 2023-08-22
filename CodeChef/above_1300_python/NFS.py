import math
from decimal import Decimal

t = int(input())

for _ in range(t):
    u, v, a, s = map(int, input().split())

    if u <= v:
        print("YES")
    else:

        possible_velocity = (u**2 - 2 * a *s)
        if possible_velocity < 0:
            print("YES")
        else:
            possible_velocity = Decimal(possible_velocity).sqrt()
            if possible_velocity > v:
                print("NO")
            else:
                print("YES")
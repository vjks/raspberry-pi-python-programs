t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    b_c_fight = min(b, c)
    b = b - b_c_fight
    c = c - b_c_fight
    if b < 0: 
        b = 0
    if c < 0:
        c = 0
    
    c_a_fight = min(c, a)
    c = c - c_a_fight
    a = a - c_a_fight
    if c < 0:
        c = 0
    if a < 0:
        a < 0
    
    a_b_fight = min(a, b)
    a = a - a_b_fight
    b = b - a_b_fight
    if a < 0:
        a = 0
    if b < 0:
        b = 0
        
    if a > 0:
        print("YES")
    else: 
        print("NO")
    
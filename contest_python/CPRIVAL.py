r1, r2 = map(int, input().split())
d1, d2 = map(int, input().split())


dom = r1 + d1
ever = r2 + d2

if dom > ever:
    print('Dominater')
else:
    print('Everule')
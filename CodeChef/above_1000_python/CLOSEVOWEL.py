import math
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    count = 0
    for x in s:
        if x == 'c' or x == 'r' or x == 'g' or x == 'l':
            count += 1
    if count == 0:
        print(1)
    else:
        mod = 1000000007
        print(2 ** count % mod)
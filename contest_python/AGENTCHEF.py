import math
t = int(input())

for _ in range(t):
    x = int(input())
    
    c = .20 * x
    print(math.ceil(100 / c))
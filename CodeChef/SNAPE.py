import math

tests = int(input())

for _ in range(tests):
    b, ls = map(int, input().split())
    
    min_value = math.sqrt(ls * ls - b * b)
    max_value = math.sqrt(b * b + ls * ls)
    
    print(min_value, max_value)
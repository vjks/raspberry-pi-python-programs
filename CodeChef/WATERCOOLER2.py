import math
tests = int(input())

for _ in range(tests):
    rental_cost, purchase_cost = map(int, input().split())
    
    print(math.ceil(purchase_cost / rental_cost) - 1)
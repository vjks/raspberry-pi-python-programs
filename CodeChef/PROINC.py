import math

num_tests = int(input())

for x in range(num_tests):
    fruit_price, profit = map(int, input().split())
    increased_price = math.floor(fruit_price * .1 + fruit_price)
    
    print(increased_price - (fruit_price - profit))
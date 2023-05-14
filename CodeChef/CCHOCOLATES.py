import math

num_tests = int(input())

for x in range(num_tests):
    coins_5, coins_10, total_money = map(int, input().split())
    num_chocolates = ((coins_5 * 5) + (coins_10 * 10)) / total_money
    print(math.floor(num_chocolates))
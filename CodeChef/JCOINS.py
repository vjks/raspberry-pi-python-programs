tests = int(input())

for x in range(tests):
    ten_rupee_coins, five_rupee_coins = map(int, input().split())
    print(ten_rupee_coins * 10 + five_rupee_coins * 5)
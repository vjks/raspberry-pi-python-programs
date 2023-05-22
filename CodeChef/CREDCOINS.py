tests = int(input())

for x in range(tests):
    coins_x, bills_num = map(int, input().split())
    print(bills_num * coins_x // 100)
    
tests = int(input())

for x in range(tests):
    bikes_num, cars_num = map(int, input().split())
    print(bikes_num * 2 + cars_num * 4)
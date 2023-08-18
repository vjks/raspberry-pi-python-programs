tests = int(input())

for _ in range(tests):
    friends_num, shoes_num = map(int, input().split())
    if shoes_num > friends_num:
        print(friends_num)
    elif shoes_num < friends_num:
        print((friends_num * 2) - shoes_num)
    else:
        print(shoes_num)
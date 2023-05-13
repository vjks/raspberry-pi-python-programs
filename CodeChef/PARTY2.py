num_tests = int(input())

for x in range(num_tests):
    friends_num, burger_cost, chefs_money = map(int, input().split())
    print(friends_num, burger_cost, chefs_money)
    if friends_num * burger_cost > chefs_money:
        print("NO")
    else:
        print("YES")
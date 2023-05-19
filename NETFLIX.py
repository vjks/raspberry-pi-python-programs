num_tests = int(input())

for x in range(num_tests):
    alice_money, bob_money, charlie_money, sub_cost = map(int, input().split())
    if alice_money + bob_money >= sub_cost:
        print("YES")
    elif bob_money + charlie_money >= sub_cost:
        print("YES")
    elif charlie_money + alice_money >= sub_cost:
        print("YES")
    else:
        print("NO")
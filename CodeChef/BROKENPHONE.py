num_tests = int(input())

for x in range(num_tests): 
    repair_cost, purchase_cost = map(int, input().split())
    if repair_cost < purchase_cost:
        print("REPAIR")
    elif purchase_cost < repair_cost:
        print("NEW PHONE")
    else:
        print("ANY")
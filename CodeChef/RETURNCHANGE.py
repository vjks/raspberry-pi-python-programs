tests = int(input())

for _ in range(tests):
    item_cost = int(input())
    remainder = item_cost % 10

    if remainder >= 5:
        item_cost += 10 - remainder
    elif remainder < 5 and remainder > 0:
        item_cost -= remainder
        
    print(100 - item_cost)
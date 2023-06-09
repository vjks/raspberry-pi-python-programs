tests = int(input())

for _ in range(tests):
    items_bought, cost_item = map(int, input().split())
    
    total_cost = items_bought * cost_item
    
    if total_cost > 9999 and total_cost <= 99999:
        print("YES")
    else:
        print("NO")
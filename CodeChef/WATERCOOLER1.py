num_tests = int(input())

for x in range(num_tests):
    cooler_rent, purchase_cost, months = map(int, input().split())
    if cooler_rent * months < purchase_cost:
        print("YES")
    else: 
        print("NO")
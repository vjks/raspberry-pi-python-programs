test_cases = int(input())

for x in range(test_cases): 
    water_amount = int(input())
    if water_amount >= 2000:
        print("YES")
    else:
        print("NO")
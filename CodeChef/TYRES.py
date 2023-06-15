import math

tests = int(input())

for _ in range(tests):
    num_tyres = int(input())
    
    if num_tyres % 4 == 0:
        print("NO")
    else:
        tyres_remaining = num_tyres % 4
        if num_tyres >= 2:
            print("YES")
        else:
            print("NO")
    
    
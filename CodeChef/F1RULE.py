import math

tests = int(input())

for x in range(tests):
    fastest, chefs = map(int, input().split())
    if (math.ceil(chefs / fastest  * 100)) <= 107:
        print("YES")
    else:
        print("NO")
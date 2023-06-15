import math
tests = int(input())

for _ in range(tests):
    members, voters = map(int, input().split())
    
    if voters % 2 == 0:
        print(math.ceil(voters / 2) + 1)
    else:
        print(math.ceil(voters / 2))
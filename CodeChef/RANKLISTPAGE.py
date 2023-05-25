import math
num_tests = int(input())

for x in range(num_tests):
    rank = int(input())
    print(math.ceil(rank / 25))
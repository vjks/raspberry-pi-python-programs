import math

T = int(input())

for x in range(T):
    group_size, sub_cost = map(int, input().split())
    num_groups = math.ceil(group_size / 6)
    print(num_groups * sub_cost)
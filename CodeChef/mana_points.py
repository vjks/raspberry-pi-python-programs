import math

num_tests = int(input())

for x in range(num_tests):
    points = input().split()
    cost_of_special_attack = int(points[0])
    current_mana_points = int(points[1])
    print(math.floor(current_mana_points / cost_of_special_attack))
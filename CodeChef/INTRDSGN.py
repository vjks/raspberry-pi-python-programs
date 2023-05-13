num_tests = int(input())

for x in range(num_tests):
    cost_floor1, cost_walls1, cost_floor2, cost_walls2 = map(int, input().split())
    option1 = cost_floor1 + cost_walls1
    option2 = cost_floor2 + cost_walls2
    if option1 < option2:
        print(option1)
    else:
        print(option2)
    
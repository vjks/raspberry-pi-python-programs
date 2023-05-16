num_tests = int(input())

for x in range(num_tests):
    budget = int(input())
    leftover_budget = budget / 2
    print(int(leftover_budget / 5 * 1000))
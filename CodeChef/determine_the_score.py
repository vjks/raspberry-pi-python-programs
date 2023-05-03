num_test_cases = int(input())

for x in range(num_test_cases):
    test_case = input().split()
    total_points = int(test_case[0])
    passed_cases = int(test_case[1])
    points_per_case = int( total_points / 10 )
    print( passed_cases * points_per_case)
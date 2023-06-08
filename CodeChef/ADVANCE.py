tests = int(input())

for _ in range(tests):
    a_time, b_time = map(int, input().split())
    # The points deducted for the 2nd problem will be the sum of the time taken 
    # for both problems.
    solve_a_b = (500 - a_time * 2) + (1000 - (b_time + a_time) * 4)
    solve_b_a = (1000 - b_time * 4) + (500 - (a_time + b_time) * 2)
    if solve_a_b > solve_b_a:
        print(solve_a_b)
    else:
        print(solve_b_a)
num_tests = int(input())

for x in range(num_tests):
    current_rating, problem_difficulty = map(int, input().split())
    if problem_difficulty >= current_rating and problem_difficulty <= (current_rating + 200):
        print("YES")
    else:
        print("NO")
num_tests = int(input())

for x in range(num_tests):
    current_rating, problem_difficulty = map(int, input().split())
    if current_rating <= problem_difficulty + 200:
        print("YES")
    else:
        print("NO")
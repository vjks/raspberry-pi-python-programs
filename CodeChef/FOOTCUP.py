num_tests = int(input())

for x in range(num_tests):
    first_team_goals, second_team_goals = map(int, input().split())
    
    if first_team_goals == second_team_goals:
        if (first_team_goals > 0 or second_team_goals > 0):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
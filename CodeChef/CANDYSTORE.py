num_tests = int(input())

for x in range(num_tests):
    daily_goal, sells = map(int, input().split())
    if sells > daily_goal:
        extra = sells - daily_goal
        print(daily_goal + extra * 2)
    else:
        print(sells)
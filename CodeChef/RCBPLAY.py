tests = int(input())

for _ in range(tests):
    rcb_points, points_needed, games_left = map(int, input().split())
    
    if rcb_points >= points_needed:
        print("YES")
    elif points_needed <= rcb_points + games_left:
        print("YES")
    elif points_needed <= rcb_points + games_left * 2:
        print("YES")
    else:
        print("NO")
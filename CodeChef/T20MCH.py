team_a_score, overs_played, runs_scored = map(int, input().split())

balls_remaining = (20 - overs_played) * 6

if((balls_remaining * 6) + runs_scored) > team_a_score:
    print("YES")
else:
    
    print("NO")
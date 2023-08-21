t = int(input())

for _ in range(t):
    d_dsa, d_toc, d_dm = map(int, input().split())
    s_dsa, s_toc, s_dm = map(int, input().split())
    
    d_total = d_dsa + d_toc + d_dm
    s_total = s_dsa + s_toc + s_dm
    
    winner = "tie"
    
    if d_total > s_total:
        winner = "dragon"
    elif s_total > d_total:
        winner = "sloth"
    else:
        if d_dsa > s_dsa:
            winner = "dragon"
        elif s_dsa > d_dsa:
            winner = "sloth"
        elif d_toc > s_toc:
            winner = "dragon"
        elif s_toc > d_toc:
            winner = "sloth"
                
    print(winner)
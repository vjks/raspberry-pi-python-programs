t = int(input())

for _ in range(t):
    s = int(input())
    q = list(map(int, input().split())) # duration of the intro song
    
    time_total = 0
    for j in range(s):
        e_l = list(map(int, input().split()))
        
        episodes = e_l[0]
        for i in range(1, episodes + 1):
            time_total += e_l[i]
        if episodes > 1:
            time_total -= (q[j] * (episodes - 1))
        
    print(time_total)
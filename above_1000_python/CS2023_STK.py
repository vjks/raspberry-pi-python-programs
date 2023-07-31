# cook your dish here
t = int(input())

for _ in range(t):
    n = int(input())
    om_solutions = list(map(int, input().split()))
    addy_solutions = list(map(int, input().split()))
    
    om_streak = addy_streak = 0
    om_current = addy_current = 0
    for _ in range(n):
        if om_solutions[_] > 0:
            om_current += 1
            if om_current > om_streak:
                om_streak += 1
        else:
            om_current = 0
        
        if addy_solutions[_] > 0:
            addy_current += 1
            if addy_current > addy_streak:
                addy_streak += 1
        else:
            addy_current = 0
                
    if om_streak > addy_streak:
        print("OM")
    elif addy_streak > om_streak:
        print("ADDY")
    else:
        print("DRAW")
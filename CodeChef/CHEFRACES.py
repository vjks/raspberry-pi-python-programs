tests = int(input())

for _ in range(tests):
    chef_race1, chef_race2, rival_race1, rival_race2 = map(int, input().split())
    medals = 0
    if chef_race1 != rival_race1 and chef_race1 != rival_race2:
        medals += 1
    
    if chef_race2 != rival_race1 and chef_race2 != rival_race2:
        medals += 1
    
    print(medals)
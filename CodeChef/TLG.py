tests = int(input())

player1_total = 0
player2_total = 0
lead_player1 = 0
lead_player2 = 0
for _ in range(tests):
    score1, score2 = map(int, input().split())
    
    player1_total = player1_total + score1
    player2_total = player2_total + score2
    
    if player1_total > player2_total:
        round_lead = player1_total - player2_total
        if round_lead > lead_player1:
            lead_player1 = round_lead
    else:
        round_lead = player2_total - player1_total
        if round_lead > lead_player2:
            lead_player2 = round_lead

if lead_player1 > lead_player2:
    print(1, lead_player1)
else:
    print(2, lead_player2)
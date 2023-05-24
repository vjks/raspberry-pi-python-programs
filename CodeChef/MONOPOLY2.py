tests = int(input())

for x in range(tests):
    p_profit, q_profit, r_profit, s_profit = map(int, input().split())
    monopoly = False
    if p_profit > q_profit + r_profit + s_profit:
        monopoly = True
    if q_profit > r_profit + s_profit + p_profit:
        monopoly = True
    if r_profit > s_profit + p_profit + q_profit:
        monopoly = True
    if s_profit > p_profit + q_profit + r_profit:
        monopoly = True
    if monopoly:
        print("YES")
    else:
        print("NO")
num_tests = int(input())

points_to_win = 7
for x in range(num_tests):
    alice_score, bob_score = map(int, input().split())
    win_alice = points_to_win - alice_score
    win_bob = points_to_win - bob_score
    if win_alice < win_bob:
        print(win_alice)
    else:
        print(win_bob)
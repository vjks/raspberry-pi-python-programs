num_tests = int(input())

for x in range(num_tests):
    prizes = input().split()
    top_10 = int(prizes[0])
    next_90 = int(prizes[1])
    print( 10 * top_10 + 90 * next_90)
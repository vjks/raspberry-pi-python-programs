import math

num_tests = int(input())

min_time_chess_game = 20
for x in range(num_tests):
    num_free_time = int(input())
    print(math.floor((num_free_time * 60) / min_time_chess_game))
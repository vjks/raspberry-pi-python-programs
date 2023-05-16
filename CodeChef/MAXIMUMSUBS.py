import math

num_tests = int(input())

for x in range(num_tests):
    duration = int(input())
    duration = duration * 60
    print(math.floor(duration / 30))
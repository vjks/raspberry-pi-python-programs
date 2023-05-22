import math
tests = int(input())

for x in range(tests):
    friends_num, slice_num = map(int, input().split())
    print(math.ceil(friends_num * slice_num / 4))
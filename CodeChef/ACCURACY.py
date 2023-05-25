import math
tests  = int(input())

for x in range(tests):
    marks = int(input())
    correct = math.ceil(marks / 3)
    print(correct * 3 - marks)
import math

tests = int(input())

for _ in range(tests):
    length = int(input())
    string = input()
    index = math.floor(length / 2)
    
    if string[0 : index] == string[index : length]:
        print("YES")
    else:
        print("NO")
    
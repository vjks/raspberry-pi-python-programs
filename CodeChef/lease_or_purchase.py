num_tests = int(input())

for x in range(num_tests):
    inputs = input().split()
    A = int(inputs[0])
    B = int(inputs[1])
    if A >= B:
        print(0)
    else:
        print(B//A)
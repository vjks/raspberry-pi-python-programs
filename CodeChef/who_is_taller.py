num_tests = int(input())

for x in range(num_tests):
    x_and_y = input().split()
    x = int(x_and_y[0])
    y = int(x_and_y[1])
    if x > y:
        print("A")
    else:
        print("B")
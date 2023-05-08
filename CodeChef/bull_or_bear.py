num_tests = int(input())

for x in range(num_tests):
    values = input().split()
    bought = int(values[0])
    sold = int(values[1])
    if bought > sold:
        print("LOSS")
    elif sold > bought:
        print("PROFIT")
    else:
        print("NEUTRAL")
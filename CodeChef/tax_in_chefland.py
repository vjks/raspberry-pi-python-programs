num_tests = int(input())

for x in range(num_tests):
    income = int(input())
    if income > 100:
        print( income - 10 )
    else:
        print( income )
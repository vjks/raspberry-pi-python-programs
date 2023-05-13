num_cases = int(input())

for x in range(num_cases):
    x_and_y = input().split()
    students_interested = int(x_and_y[1])
    num_seats_math = int(x_and_y[0])
    if num_seats_math < students_interested:
        extra_seats = students_interested - num_seats_math
        print(extra_seats)
    else:
        print(0)
        
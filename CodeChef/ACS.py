tests = int(input())

for _ in range(tests):
    points = int(input())
    
    count = 0
    if(points % 100 == 0 and points >= 100):
        count = points // 100
    elif points > 100 and points < 1000:
        third_digit = points % 10
        points = points // 10
        second_digit = points % 10
        points = points // 10
        first_digit = points % 10
        if second_digit == 0 and first_digit + third_digit <= 10:
            count = first_digit + third_digit
        else:
            count = -1
    elif points >= 0 and points <= 10:
        count = points
    else:
        count = -1
    print(count)
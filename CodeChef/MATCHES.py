def stick_calculator(digit):
    if digit == 0:
        return 6
    elif digit == 1:
        return 2
    elif digit == 2:
        return 5
    elif digit == 3:
        return 5
    elif digit == 4:
        return 4
    elif digit == 5:
        return 5
    elif digit == 6:
        return 6
    elif digit == 7:
        return 3
    elif digit == 8:
        return 7
    elif digit == 9: 
        return 6
    else:
        return "ERROR"
for _ in range(int(input())):
    a, b = map(int, input().split())
    
    total = a + b
    
    if total == 0:
        print(6)
    else:
        sticks = 0
        while total != 0:
            digit = total % 10
            sticks += stick_calculator(digit)
            total = int(total / 10)
        print(sticks)
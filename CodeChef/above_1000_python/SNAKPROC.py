r = int(input())

for _ in range(r):
    l = int(input())
    string = input()
    
    stack = []
    for _ in string:
        if _ == 'H':
            stack.append(_)
        elif _ == 'T':
            stack.append(_)
    
    if len(stack) == 0:
        print("Valid")
    elif len(stack) % 2 != 0:
        print("Invalid")
    elif len(stack) >= 2:
        status = "Valid"
        while stack:
            a = stack.pop()
            b = stack.pop()
            if a != 'T' or b != 'H':
                status = "Invalid"
                break
        print(status)
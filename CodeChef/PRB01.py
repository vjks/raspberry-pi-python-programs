tests = int(input())

for _ in range(tests):
    number = int(input())
    prime = True
    for _ in range(2, number - 1):
        if number % _ == 0:
            prime = False
    if prime and number != 1:
        print("yes")
    elif number == 1:
        print("no")
    else:
        print("no")
T = int(input())

for x in range(T):
    A = int(input())
    if A % 7 == 0 and A % 2 == 0:
        print("Alice")
    elif A % 9 == 0 and A % 2 != 0:
        print("Bob")
    else:
        print("Charlie")
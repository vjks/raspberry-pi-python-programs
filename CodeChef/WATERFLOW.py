tests = int(input())

for x in range (tests):
    initial, capacity, rate, hours = map(int, input().split())
    left = capacity - initial
    new_water = rate * hours
    if new_water > left:
        print("Overflow")
    elif new_water < left: 
        print("Unfilled")
    elif new_water == left:
        print("Filled")
    else:
        print("Error")
    
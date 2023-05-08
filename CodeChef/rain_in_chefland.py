num_tests = int(input())

for x in range(num_tests):
    rain = int(input())
    if rain < 3:
        print("LIGHT")
    elif rain >= 3 and rain < 7:
        print("MODERATE")
    elif rain >= 7:
        print("HEAVY")
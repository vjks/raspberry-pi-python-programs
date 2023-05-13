num_tests = int(input())

for x in range(num_tests):
    spice_level = int(input())
    if spice_level < 4:
        print("MILD")
    elif spice_level >= 4 and spice_level < 7:
        print("MEDIUM")
    elif spice_level >= 7:
        print("HOT")
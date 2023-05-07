num_tests = int(input())

for x in range(num_tests):
    battery_health = int(input())
    if battery_health >= 80:
        print("YES")
    else:
        print("NO")
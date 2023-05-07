num_cases = int(input())

for x in range(num_cases):
    speeds = input().split()
    jerry_speed = int(speeds[0])
    tom_speed = int(speeds[1])
    if tom_speed > jerry_speed:
        print("YES")
    else:
        print("NO")
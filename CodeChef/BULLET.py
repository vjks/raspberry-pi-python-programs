tests = int(input())

for _ in range(tests):
    bullet_speed, distance, time = map(int, input().split())
    time_taken = distance // bullet_speed
    if time - time_taken < 0:
        print(0)
    else:
        print(time - time_taken)
        
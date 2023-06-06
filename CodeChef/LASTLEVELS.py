tests = int(input())

for _ in range(tests):
    levels_remaining, time_per_level, break_time = map(int, input().split())
    
    time = levels_remaining * time_per_level
    if levels_remaining % 3 == 0:
        extra_time = ((levels_remaining // 3) - 1) * break_time
    else:
        extra_time = (levels_remaining // 3 ) * break_time
    print(time + extra_time)
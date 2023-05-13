num_tests = int(input())

for x in range(num_tests):
    time_slept = int(input())
    sleep_deprived_limit = 7
    if time_slept < sleep_deprived_limit:
        print("YES")
    else:
        print("NO")
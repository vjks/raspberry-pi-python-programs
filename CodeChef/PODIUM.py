num_tests = int(input())

for x in range(num_tests):
    times = input().split()
    time_a = int(times[0])
    time_b = int(times[1])
    print(time_a + time_b)
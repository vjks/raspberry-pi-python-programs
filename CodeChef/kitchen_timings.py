num_tests = int(input())

for x in range(num_tests):
    start_end_times = input().split()
    start = int(start_end_times[0])
    end = int(start_end_times[1])
    print( end - start )
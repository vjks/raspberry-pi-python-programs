num_tests = int(input())

for x in range(num_tests):
    plate_length, plate_width, cost_per_cm = map(int, input().split())
    print((plate_width + plate_length) * 2 * cost_per_cm)
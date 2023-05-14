num_tests = int(input())

for x in range(num_tests):
    current_volume, future_volume = map(int, input().split())
    print(abs(future_volume - current_volume))
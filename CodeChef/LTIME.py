num_tests = int(input())

for x in range(num_tests):
    current_time = int(input())
    if current_time >= 1 and current_time <= 4:
        print("YES")
    else:
        print("NO")
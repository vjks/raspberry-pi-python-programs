num_tests = int(input())

show_length = 24
for x in range(num_tests):
    time_left = int(input())
    if time_left > show_length:
        print("YES")
    else:
        print("NO")
num_cases = int(input())

min_time_taken = 30
for x in range(num_cases):
    time = int(input())
    if time >= min_time_taken:
        print("YES")
    else:
        print("NO")
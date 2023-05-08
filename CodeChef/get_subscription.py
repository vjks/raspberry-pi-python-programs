num_cases = int(input())

for x in range(num_cases):
    meeting_time = int(input())
    if meeting_time > 30:
        print("YES")
    else:
        print("NO")
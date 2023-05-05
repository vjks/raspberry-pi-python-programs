num_cases = int(input())

for x in range(num_cases):
    rank = int(input())
    if rank <= 10:
        print("YES")
    else:
        print("NO")
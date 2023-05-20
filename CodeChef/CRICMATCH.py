num_tests = int(input())

for x in range(num_tests):
    num_runs, num_overs = map(int, input().split())
    if num_overs * 6 * 6 >= num_runs:
        print("YES")
    else:
        print("NO")
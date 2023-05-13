num_tests = int(input())

for x in range(num_tests):
    interest_rate, inflation_rate = map(int, input().split())
    if interest_rate >= inflation_rate * 2:
        print("YES")
    else:
        print("NO")
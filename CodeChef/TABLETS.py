num_tests = int(input())

for x in range(num_tests):
    totake_days, tablets = map(int, input().split())
    if totake_days * 3 <= tablets:
        print("YES")
    else:
        print("NO")
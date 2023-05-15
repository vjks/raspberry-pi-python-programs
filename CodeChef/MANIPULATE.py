num_tests = int(input())

for x in range(num_tests):
    max_guards, current_guards = map(int, input().split())
    if current_guards <= max_guards:
        print("YES")
    else:
        print("NO")
num_tests = int(input())

for x in range(num_tests):
    A_comparisons, B_comparisons = map(int, input().split())
    if A_comparisons > B_comparisons:
        print("YES")
    else:
        print("NO")
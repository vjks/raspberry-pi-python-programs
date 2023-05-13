num_tests = int(input())

for x in range(num_tests):
    X, Y, Z = map(int, input().split())
    print(X * Y * Z)
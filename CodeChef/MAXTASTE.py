tests = int(input())

for x in range(tests):
    a_tastiness, b_tastiness, c_tastiness, d_tastiness = map(int, input().split())
    first_ingridient = max(a_tastiness, b_tastiness)
    second_ingridient = max(c_tastiness, d_tastiness)
    print(first_ingridient + second_ingridient)
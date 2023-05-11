num_tests = int(input())

for x in range(num_tests):
    girls_boys = input().split()
    num_girls = int(girls_boys[0])
    num_boys = int(girls_boys[1])
    print(num_boys - num_girls)
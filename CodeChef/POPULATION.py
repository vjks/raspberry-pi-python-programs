num_tests = int(input())

for x in range(num_tests):
    num_town_people, num_left, num_immigrated = map(int, input().split())
    print(num_town_people - num_left + num_immigrated)
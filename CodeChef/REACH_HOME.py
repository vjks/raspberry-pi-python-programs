num_tests = int(input())

for x in range(num_tests):
    litres_fuel, distance_home = map(int, input().split())
    if litres_fuel * 5 >= distance_home:
        print("YES")
    else:
        print("NO")
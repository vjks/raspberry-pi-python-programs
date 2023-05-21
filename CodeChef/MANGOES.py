num_tests = int(input())

for x in range(num_tests):
    mango_weight, truck_weight, bridge_tolerance = map(int, input().split())
    print((bridge_tolerance - truck_weight) // mango_weight)
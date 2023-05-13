num_tests = int(input())

for x in range(num_tests):
    distance_travelled = int(input())
    if distance_travelled <= 300:
        print(300 * 10)
    elif distance_travelled > 300:
        print( distance_travelled * 10)
num_tests = int(input())

for x in range(num_tests):
    car_speed = int(input())
    if car_speed > 70 and car_speed <= 100:
        print(500)
    elif car_speed > 100:
        print(2000)
    else:
        print(0)
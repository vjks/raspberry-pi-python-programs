tests = int(input())
mario_status = ["NORMAL", "HUGE", "SMALL"]
for _ in range(tests):
    mushroom_num = int(input())
    iterator = 0
    for x in range(mushroom_num):
        if iterator == 2:
            iterator = 0
        else:
            iterator = iterator + 1
    print(mario_status[iterator])
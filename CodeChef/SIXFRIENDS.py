num_tests = int(input())

for x in range(num_tests):
    double_room_cost, triple_room_cost = map(int, input().split())
    double_room_total = double_room_cost * 3
    triple_room_total = triple_room_cost * 2
    if double_room_total < triple_room_total:
        print(double_room_total)
    else:
        print(triple_room_total)
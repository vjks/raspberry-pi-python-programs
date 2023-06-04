tests = int(input())

for _ in range(tests): 
    bottles_num, capacity_bottle, tank_capacity = map(int, input().split())
    sum = 0
    for y  in range(bottles_num):
        if (y + 1) * capacity_bottle <= tank_capacity:
            sum += 1        
    print(sum)
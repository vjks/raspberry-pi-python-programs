t = int(input())

for _ in range(t):
    x1, x2, x3, v1, v2 = map(int, input().split())
    
    # time = distance / speed
    
    chef_time = abs(x3 - x1) / v1
    kefa_time = abs(x3 - x2) / v2
    
    if chef_time < kefa_time:
        print("Chef")
    elif kefa_time < chef_time:
        print("Kefa")
    else:
        print("Draw")
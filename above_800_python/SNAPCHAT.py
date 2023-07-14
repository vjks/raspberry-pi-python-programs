t = int(input())

for _ in range(t):
    n = int(input())
    chef_snaps = list(map(int, input().split()))
    chefina_snaps = list(map(int, input().split()))
    
    count = 0
    biggest_count = 0
    for x in range(n):
        if chef_snaps[x] > 0 and chefina_snaps[x] > 0:
            count += 1
            if count >= biggest_count:
                biggest_count = count
        else:
            count = 0
    print(biggest_count)
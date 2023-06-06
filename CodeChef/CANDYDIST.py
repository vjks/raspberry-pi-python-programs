tests = int(input())

for _ in range(tests):
    candies_num, friends_num = map(int, input().split())
    
    if (candies_num / friends_num) % 2 == 0:
        print("YES")
    else:
        print("NO")
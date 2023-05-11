num_tests = int(input())

for x in range(num_tests):
    friends_passes = input().split()
    
    friends = int(friends_passes[0])
    passes = int(friends_passes[1])
    if passes >= (friends + 1):
        print("YES")
    else:
        print("NO")
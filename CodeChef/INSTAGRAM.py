num_tests = int(input())

for x in range(num_tests):
    following, follower_count = map(int, input().split())
    if following > (follower_count * 10):
        print("YES")
    else:
        print("NO")
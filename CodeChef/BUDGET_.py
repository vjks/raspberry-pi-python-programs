num_tests = int(input())

for x in range(num_tests):
    amount, expediture = map(int, input().split())
    if(30 * expediture <= amount):
        print("YES")
    else:
        print("NO")
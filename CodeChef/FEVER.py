num_tests = int(input())
normal_temp = 98

for x in range(num_tests):
    chef_temp = int(input())
    if chef_temp > normal_temp:
        print("YES")
    else:
        print("NO")
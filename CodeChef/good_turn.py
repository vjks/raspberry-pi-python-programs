num_cases = int(input())

for x in range(num_cases):
    line = input()
    nums = line.split()
    
    num1 = int(nums[0])
    num2 = int(nums[1])
    
    if num1 + num2 > 6:
        print("YES")
    else:
        print("NO")
num_tests = int(input())

for x in range(num_tests):
    nums = input().split()
    a = int(nums[0])
    b = int(nums[1])
    c = int(nums[2])
    
    max_a_b = max(a, b)
    max_a_b_c = max(max_a_b, c)
    
    min_a_b = min(a, b)
    min_a_b_c = min(min_a_b, c)
    
    print(max_a_b_c - min_a_b_c)
    
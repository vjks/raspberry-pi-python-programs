num_cases = int(input())

for x in range(num_cases):
    single_line = input().split()
    num_X = single_line[0]
    num_Y = single_line[1]
    num_A = single_line[2]
    #print(num_X, num_Y, num_A)
    if num_A >= num_X:
        if num_A < num_Y:
            print("YES")
        else:
            print("NO") # The given age is greater than or equal to the required max age.
    else:
        print("NO") # The given age might me less than the required age.
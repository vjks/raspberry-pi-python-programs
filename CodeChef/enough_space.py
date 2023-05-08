num_cases = int(input())

for x in range(num_cases):
    space_and_files = input().split()
    free_space = int(space_and_files[0])
    num_files_1 = int(space_and_files[1])
    num_files_2 = int(space_and_files[2])
    if free_space >= num_files_1 + num_files_2 * 2:
        print("YES")
    else:
        print("NO")
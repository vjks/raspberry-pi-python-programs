num_cases = int(input())

for x in range(num_cases):
    heights = input().split()
    son_height = int(heights[0])
    min_height = int(heights[1])
    if son_height >= min_height:
        print("YES")
    else:
        print("NO")
tests = int(input())

for x in range(tests):
    a, b, c = map(int, input().split())
    temp_min = max(a, c)
    if(temp_min >= a and temp_min <= b and temp_min >= c): 
        print("YES")
    else:
        print("NO")
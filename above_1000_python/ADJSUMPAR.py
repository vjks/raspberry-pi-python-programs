t = int(input())

for _ in range(t):
    n = int(input())
    array_b = list(map(int, input().split()))
    
    one_count = array_b.count(1)
    
    if one_count % 2 == 0:
        print("yes")
    else:
        print("no")
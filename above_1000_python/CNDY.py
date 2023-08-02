t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    
    distinct = "YES"
    for _ in array:
        if array.count(_) > 2:
            distinct = "NO"
    
    print(distinct)
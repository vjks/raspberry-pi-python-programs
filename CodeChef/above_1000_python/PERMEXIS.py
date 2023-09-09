for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    reorganize = True
    
    i = 0
    while(i < n - 1):
        if abs(a[i + 1] - a[i]) > 1:
            reorganize = False
            break
        i += 1
    
    if reorganize:
        print("YES")
    else:
        print("NO")
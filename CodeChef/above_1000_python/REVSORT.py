for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    b = a[:]
    b.sort()
    

    if a == b:
        sort = True
    else:
        sort = False
    
    cond = True
    for _ in range(n - 1):
        if sort:
            break
        
        if a[_] > a[_ + 1]:
            greater = True
        else:
            greater = False
        
        if a[_] + a[_ + 1] > x:
            exceeds = True
        else:
            exceeds = False
            
        if greater and exceeds:
            cond = False
            break
        elif greater and not exceeds:
            temp = a[_]
            a[_] = a[_ + 1]
            a[_ + 1] = temp
        
    if cond:
        print("YES")
    else:
        print("NO")
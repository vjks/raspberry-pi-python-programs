for _ in range(int(input())):
    a, b, c, d, k = map(int, input().split())
    
    y_change = abs(d - b)
    x_change = abs(c - a)
    total_change = x_change + y_change
    
    if total_change == k:
        print("YES")
    elif total_change > k:
        print("NO")
    elif (k - total_change) % 2 == 0:
        print("YES")
    elif (k - total_change) % 2 == 1:
        print("NO")
    else:
        print("ERROR")
        

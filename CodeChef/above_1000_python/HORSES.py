for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    
    s.sort()
    
    smallest = s[1] - s[0]
    for j in range(n - 1):
        diff = s[j + 1] - s[j]
        if diff < smallest:
            smallest = diff
            
    print(smallest)
t = int(input())

for _ in range(t):
    n, k, l = map(int, input().split())
    a = list(map(int, input().split()))
    
    a.sort(reverse=True)
    #print(a)
    total = 0
    pos = 1
    while pos <= n:
        if pos == l:   
            total += a[pos - 1]
            l += k 
        pos += 1
    print(total)
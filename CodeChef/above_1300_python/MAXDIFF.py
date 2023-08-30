for _ in range(int(input())):
    n, k = map(int, input().split())
    w = list(map(int, input().split()))
    
    w.sort()
    
    i = 0
    j = n - 1
    w1 = w2 = w3 = w4 = 0
    while(i < n):
        if i < k:
            w1 += w[i]
        else:
            w2 += w[i]
        
        if j >= n - k:
            w3 += w[j]
        else:
            w4 += w[j]
        i+=1
        j-=1
    
    possible1 = abs(w1 - w2)
    possible2 = abs (w3 - w4)
    
    print(max(possible1, possible2))
    
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    
    count = 0
    j = 0
    while j < (n - k + 1):
        i = j
        nap = False
        while i < j + k:
            if int(s[i]) == 0:
                nap = True
            else:
                nap = False
                break
            i += 1
        if nap: 
            count += 1
            j += k
        else:
            j += 1
    print(count)
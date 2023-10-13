import math
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    count = 0
    i = 0
    
    while i < n:
        if i == n - 1 and int(s[i]) == 0 and int(s[i - 1]) == 0 :
            count += 1
            i += 1
        elif i == 0 and int(s[i]) == 0 and int(s[i + 1]) == 0:
            count += 1
            i += 2
        elif i > 0 and int(s[i]) == 0 and int(s[i + 1]) == 0 and int(s[i - 1]) == 0:
            count += 1
            i += 2
        elif int(s[i]) == 1:
            i += 2
        else:
            i += 1
    print(count)
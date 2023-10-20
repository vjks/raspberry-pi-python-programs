t = int(input())

for _ in range(t):
    s = input()
    
    first = s[0]
    last = s[len(s) - 1]
    
    l_shifted = s[1:]
    r_shifted = s[:-1]
    
    l_shifted += first
    last += r_shifted
    
    if l_shifted == last:
        print("YES")
    else:
        print("NO")
    
    
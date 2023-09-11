r = int(input())

for _ in range(r):
    l = int(input())
    s = input()
    
    stack = 0
    status = "Valid"
    
    
    for c in s:
        if c == 'H':
            stack += 1
        
        if c == 'T':
            stack -= 1
        
        if stack > 1 or stack < 0:
            status = "Invalid"
            break
        

    if stack > 0:
        status = "Invalid"
    print(status)
            
    
    
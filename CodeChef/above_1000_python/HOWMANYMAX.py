t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    s = '0' + s
    s = s + '1'
    
    count = 0
    
    for _ in range(n + 1):
        if s[_] == '0' and s[_ + 1] == '1':
            count += 1            
            
    print(count)
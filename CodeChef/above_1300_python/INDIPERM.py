t = int(input())

for _ in range(t):
    n = int(input())
    
    output = ''
    end = ' '
    for _ in range(2, n + 2):
        num = _
        if _ == n + 1:
            end = ''
            num = 1
        output += str(num) + end 
    
    if len(output) > 0:
        print(output)
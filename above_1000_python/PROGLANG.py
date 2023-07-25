t = int(input())

for _ in range(t):
    variables = list(map(int, input().split()))
    
    lang = 0
    if variables[0] == variables[2] or variables[0] == variables[3]:
        if variables[1] == variables[2] or variables[1] == variables[3]:
            lang = 1
    
    if variables[0] == variables[4] or variables[0] == variables[5]:
        if variables[1] == variables[4] or variables[1] == variables[5]:
            lang = 2
            
    print(lang)
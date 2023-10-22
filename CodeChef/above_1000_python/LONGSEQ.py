t = int(input())

for _ in range(t): 
    s = input()
    
    d = dict()
    for x in s:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
            
    count = 0
    for value in d.values():
        if value == 1:
            count += 1
    
    
    if s == "10" or s == "01":
        print("Yes")
    elif count == 1:
        print("Yes")
    else:
        print("No")
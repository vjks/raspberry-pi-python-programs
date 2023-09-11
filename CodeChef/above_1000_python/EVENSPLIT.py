for _ in range(int(input())):
    n = int(input())
    s = input()
    
    output = ""
    counter1 = counter0 = 0
    if s == "10":
        output = "10"
    else:
        for c in s:
            if c == "1":
                counter1 += 1
            else:
                counter0 += 1
    for _ in range(counter0):
        output += "0"
    
    for _ in range(counter1):
        output += "1"
    
    print(output)
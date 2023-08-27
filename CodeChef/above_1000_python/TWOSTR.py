for _ in range(int(input())):
    x = input()
    y = input()
    
    length = len(x)
    status = "Yes"
    for i in range(length):
        if x[i] != '?' and y[i] != '?':
            if x[i] != y[i]:
                status = "No"
                break
    print(status)
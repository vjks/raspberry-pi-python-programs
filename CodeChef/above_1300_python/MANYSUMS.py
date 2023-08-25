for _ in range(int(input())):
    l, r = map(int, input().split())
    
    if r - l == 0:
        print(1)
    elif r - l == 1:
        print(3)
    else:
        print((r - l) * 2 + 1)
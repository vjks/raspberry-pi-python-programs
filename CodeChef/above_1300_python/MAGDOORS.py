for _ in range(int(input())):
    S = input()
    
    n = len(S)
    wand_use = 0
    if S[0] == '0':
        wand_use += 1
    for _ in range(n - 1):
        if S[_] != S[_ + 1]:
            wand_use += 1
    print(wand_use)
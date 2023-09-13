for _ in range(int(input())):
    n = int(input())
    s = input()
    
    if s[0] == "1":
        new = "1"
        for _ in range(n - 1):
            new += "0"
        print(new)
    elif s[0] == "0":
        pos = s.find("1")
        if pos > n - 3:
            print(s)
        else:
            new = ""
            for _ in range(n):
                if _ == pos:
                    new += "1"
                else:
                    new += "0"
            print(new)
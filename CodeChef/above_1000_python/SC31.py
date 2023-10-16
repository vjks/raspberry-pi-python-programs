t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    
    for _ in range(n - 1):
        b = input()
        c = ''    
        for _ in range(10):
            c += str(int(a[_]) ^ int(b[_]))
        a = c
    print(c.count('1'))
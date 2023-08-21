t = int(input())

for _ in range(t):
    n = int(input())
    count = 0
    dolls = []
    for _ in range(n):
        dolls.append(int(input()))
    
    for _ in range(n):
        if dolls.count(dolls[_]) % 2 != 0:
            print(dolls[_])
            break
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    seq = ''
    for _ in range(0, n - 1, 2):
        if s[_] == '0' and s[_ + 1] == '0':
            seq += 'A'
        elif s[_] == '0' and s[_ + 1] == '1':
            seq += 'T'
        elif s[_] == '1' and s[_ + 1] == '0':
            seq += 'C'
        elif s[_] == '1' and s[_ + 1] == '1':
            seq += 'G'
    
    print(seq)
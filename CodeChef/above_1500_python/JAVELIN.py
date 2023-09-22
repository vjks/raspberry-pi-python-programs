t = int(input())

for _ in range(t):
    n, m, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    pos = dict()
    qualified = list()
    for mark in a:
        if mark not in pos:
            i = a.index(mark)
            pos[mark] = i + 1
            
        if mark >= m:
            qualified.append(mark)
            i = a.index(mark)
            
    
    if len(qualified) < x:
        total = len(qualified)
        a.sort(reverse=True)
        i = 0
        while total < x:
            if a[i] not in qualified:
                qualified.append(a[i])
                total += 1
            i += 1
    
    q_len = len(qualified)
    print(q_len, '', end='')
    output = ''
    for key, value in pos.items():
        if key in qualified:
            output += str(value) + ' '
    print(output.strip())
T = int(input())

for _ in range(T):
    N = int(input())
    S = input()
    
    count = 0
    x = 0
    while x < N:
        if x <= N - 2 and S[x] == S[x + 1]:
            x += 2
            count += 1
        else:
            x += 1
            count += 1
    print(count)
    
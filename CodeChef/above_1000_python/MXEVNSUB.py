t = int(input())

for _ in range(t):
    n = int(input())
    
    counter = 0
    n_sum = n * (n + 1) / 2
    for x in (range(1, n + 1)):
        if n == 1:
            print(0)
        elif int(n_sum - counter) % 2 == 0:
            print(n - counter)
            break
        else:
            counter += 1
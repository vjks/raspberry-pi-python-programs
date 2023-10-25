for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    total = sum(a)

    if total % n != 0:
        print('No')
    else:
        y = total // n
        divisible = True
        for _ in range(n):
            if (a[_] - y) % 2 != 0:
                divisible = False
                break
        if divisible:
            print('Yes')
        else:
            print('No')
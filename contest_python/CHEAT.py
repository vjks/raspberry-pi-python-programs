for _ in range(int(input())):
    n = int(input())
    
    if n == 1:
        print(0)
    else:
        count = 0
        start = 2
        
        while start <= n:
            start += 7
            count += 1
        print(count)
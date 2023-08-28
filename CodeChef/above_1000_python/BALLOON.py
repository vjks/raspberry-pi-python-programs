for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    num_problems = 0
    counter = 0
    if n == 7:
        num_problems = 7
    else:
        i = 0
        while(i < n):
            if a[i] >= 1 and a[i] <= 7 :
                counter += 1
                num_problems += 1
            else:
                num_problems += 1
            
            if counter  == 7:
                break
            i += 1
    print(num_problems)
        
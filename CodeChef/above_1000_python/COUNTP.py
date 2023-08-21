# cook your dish here
T = int(input())

total = 0
for _ in range(T):
    N = int(input())
    array = list(map(int, input().split()))
    
    total = 0
    total = sum(array)
    no_odd = False
    for _ in range(N):
        if array[_] % 2 != 0:
            no_odd = True
    
    if no_odd and total % 2 == 0:
        print("YES")
    else:
        print("NO")
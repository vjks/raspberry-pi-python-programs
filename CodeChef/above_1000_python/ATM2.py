t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    amount_withdrawn = list(map(int, input().split()))
    
    for _ in amount_withdrawn:
        if k >= _:
            k -= _
            print(1, end = '')
        else:
            print(0, end = '')
    print()
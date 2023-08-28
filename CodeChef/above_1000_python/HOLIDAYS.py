for _ in range(int(input())):
    n, w = map(int, input().split())
    money_array = list(map(int, input().split()))
    
    total = work = 0
    
    
    for _ in range(n):
        max_money = max(money_array)
        total += max_money
        if total >= w:
            work += 1
            break
        else:
            work += 1
            money_array.remove(max_money)
    print(n - work)
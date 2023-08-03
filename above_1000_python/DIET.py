t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    array_protein = list(map(int, input().split()))
    remaining = 0
    days = 1
    able = True
    for _ in array_protein:
        if k > remaining + _:
            able = False
            break
        elif k <= _:
            days += 1
            remaining += _ - k
        elif k <= remaining + _:
            days += 1
            remaining = (remaining + _) - k
            
    if able:
        print("YES")
    else:
        print("NO", days)
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    unique = set(a)
    if len(unique) == m:
        print("No")
    else:
        print("Yes")
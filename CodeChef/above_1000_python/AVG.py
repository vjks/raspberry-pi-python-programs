t = int(input())

for _ in range(t):
    n, k, v = map(int, input().split())
    
    a = list(map(int, input().split()))
    final_total = sum(a)
    
    initial_total = (n + k) * v
    
    if final_total >= initial_total:
        print(-1)
    else:
        if (initial_total - final_total) % k == 0:
            deleted = (initial_total - final_total) // k
            print(deleted)
        else:
            print(-1)
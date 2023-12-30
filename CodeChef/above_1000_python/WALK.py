t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    val = n
    
    for _ in range(n):
        if val < a[_]:
            val += a[_] - val
        val -= 1
    
    print(val + n)
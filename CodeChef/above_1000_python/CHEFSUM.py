t = int(input())

def prefixSum(i, a, previous):
    previous += a[i - 1]
    return previous

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    array_of_sums = []
    s = sum(a)
    previous = 0
    for i in range(1, n + 1):
        
        p_sum = prefixSum(i, a, previous)
        
        s_sum = s - previous
        previous = p_sum
        
        array_of_sums.append(p_sum + s_sum)
        
    print(array_of_sums.index(min(array_of_sums)) + 1)
    

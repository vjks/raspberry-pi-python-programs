for _ in range(int(input())):
    n = int(input())
    b = list(map(str, input().split()))
    
    count_a = count_b = 0
    
    count_a = b.count('A')
    count_b = b.count('B')
    
    max_chain = n - min(count_a, count_b)
    print(max_chain)
    
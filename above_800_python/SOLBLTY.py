t = int(input())

for _ in range(t):
    x, a, b = map(int, input().split())
    
    print((a + (100 - x) * b) * 10)
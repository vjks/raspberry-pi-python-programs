t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    maximum = a[n - 1]
    minimum = a[0]
    third = a[n - 2]
    
    print((maximum - minimum) * third)
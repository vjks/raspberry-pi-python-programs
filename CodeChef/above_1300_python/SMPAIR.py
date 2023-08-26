for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    smallest = min(a)
    a.remove(smallest)
    smaller = min(a)
    print(smaller + smallest)
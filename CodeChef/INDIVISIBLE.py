tests = int(input())

for _ in range(tests):
    a, b, c = map(int, input().split())
    
    for _ in range(1, 100):
        if a % _ != 0 and b % _ != 0 and c % _ != 0:
            print(_)
            break
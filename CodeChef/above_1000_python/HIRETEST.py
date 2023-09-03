t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    x, y = map(int, input().split())
    
    output = ""
    for _ in range(n):
        solves = input()
        full = partial = 0
        for _ in range(m):
            if solves[_] == 'F':
                full += 1
            elif solves[_] == 'P':
                partial  += 1
        if full >= x:
            output += "1"
        elif full >= (x - 1) and partial >= y:
            output += "1"
        else:
            output += "0"
    print(output)
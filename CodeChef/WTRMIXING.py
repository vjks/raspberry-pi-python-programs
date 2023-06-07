tests = int(input())

for _ in range(tests):
    a, b, x, y = map(int, input().split())

    if b >= (a - y) and b <= (a + x): 
        print("YES")
    else:
        print("NO")
t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    
    count = 0
    word = "EQUINOX"
    
    for _ in range(n):
        s = input()
        
        c = s[0]
        
        if c in word:
            count += 1
    
    a_points = a * count
    b_points = (n - count) * b
    
    if a_points > b_points:
        print("SARTHAK")
    elif b_points > a_points:
        print("ANURADHA")
    else:
        print("DRAW")
t = int(input())

for _ in range(t):
    n, k, l = map(int, input().split())
    s = list(map(int, input().split()))
    
    friend_speed = s[n - 1]
    
    s.pop()
    
    success = True
    if k < 0:
        for _ in range(len(s)):
            if friend_speed > s[_]:
                continue
            else:
                success = False
                break
    else:
        for _ in range(len(s)):
            if friend_speed + k * ( l - 1) > s[_]:
                continue
            else:
                success = False
                break
    if success:
        print("Yes")
    else:
        print("No")
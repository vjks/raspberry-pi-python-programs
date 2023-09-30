t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    
    #m  is ignored files
    ignored = list(map(int, input().split()))
    
    # k is tracked files
    tracked = list(map(int, input().split()))
    
    tracked_ignored = untracked_unignored = 0
    
    for _ in range(1, n + 1):
        if _ in ignored and _ in tracked:
            tracked_ignored += 1
        
        if _ not in ignored and _ not in tracked:
            untracked_unignored += 1
    
    print(tracked_ignored, untracked_unignored)
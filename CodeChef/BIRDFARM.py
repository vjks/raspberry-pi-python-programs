num_tests = int(input())

for x in range(num_tests):
    x, y, z = map(int, input().split())
    
    has_chicken = False
    has_duck = False
    
    if z % x == 0:
        has_chicken = True
    if z % y == 0:
        has_duck = True
        
    if has_chicken and has_duck:
        print("ANY")
    elif not has_chicken and not has_duck:
        print("NONE")
    elif has_chicken:
        print("CHICKEN")
    elif has_duck:
        print("DUCK")
    else:
        print("NONE")
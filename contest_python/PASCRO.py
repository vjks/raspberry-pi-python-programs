t = int(input())

for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    
    chef_count = chefina_count = ties = 0
    
    for _ in range(n):
        if a[_] == b[_]:
            ties += 1
        elif a[_] == 'R' and b[_] == 'S':
            chef_count += 1
        elif a[_] == 'P' and b[_] == 'R':
            chef_count += 1
        elif a[_] == 'S' and b[_] == 'P':
            chef_count += 1
        elif b[_] == 'R' and a[_] == 'S':
            chefina_count += 1
        elif b[_] == 'P' and a[_] == 'R':
            chefina_count += 1
        elif b[_] == 'S' and a[_] == 'P':
            chefina_count += 1
    
#print(chef_count, chefina_count, ties)
    
    if chef_count > chefina_count:
        print(0)
    elif chef_count == chefina_count:
        print(1)
    else:
        total = (n - ties) // 2 + 1 
        total -= chef_count
        print(total)
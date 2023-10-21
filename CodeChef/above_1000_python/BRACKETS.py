def find_max_balance(a):
    balance = 0
    max_balance = 0
    
    for _ in range(len(a)):
        if a[_] == '(':
            balance += 1
        
        if a[_] == ')':
            balance -= 1
            
        max_balance = max(max_balance, balance)
        
    return max_balance
    
t = int(input())

for _ in range(t):
    x = input()
    bracket_len = find_max_balance(x)
    
    for _ in range(bracket_len):
        print('(', end='')
    for _ in range(bracket_len):
        print(')', end='')
    if _ != t - 1: 
        print()
        
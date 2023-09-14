
t = int(input())

for _ in range(t):
    n = int(input())
    
    if n == 1:
        print(3)
    else:
        number = "1"
        while(n > 2):
            number += "0"
            n -= 1
        number += "5"
        
        print(int(number));
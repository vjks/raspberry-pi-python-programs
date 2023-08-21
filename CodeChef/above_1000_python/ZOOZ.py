t = int(input())

for _ in range(t):
    n = int(input())
    
    if n == 3:
        print("010")
    else:
        string = "0"
        
        print(1, end = "")
        print(string * (n - 2), end = "")
        print(1)
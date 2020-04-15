total = 0
count = 0
num = "start"

while num != "done":
    try:
        num = input("Enter a number:")
        total += int(num)    
    except:
        if( num != "done"):
            print("Invalid input")
            
print(total)
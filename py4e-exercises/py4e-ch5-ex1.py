total = 0
count = 0
average = 0
num = "start"

while num != "done":
    try:
        num = input("Enter a number:")
        total += int(num)
        count += 1
    except:
        if( num != "done"):
            print("Invalid input")
            
average = total/count
print(total, count, average)
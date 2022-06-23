maxNum = 0
minNum = 0
count = 0
num = "start"

while num != "done":
    try:
        num = input("Enter a number:")
        maxNum = max( maxNum, int(num))
        if count == 0:
            minNum = int(num)
        else:
            minNum = min( minNum, int(num))
        count += 1
    except:
        if( num != "done" ):
            print("Invalid input")
            
print(maxNum, minNum)

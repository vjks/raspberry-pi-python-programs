sizeAndNumK = input("Enter the total number of integers:")
inputList = sizeAndNumK.split()
size = inputList[0]
numK = inputList[1]
print("Size is: " + size + " Number of elements is: " + numK)
values = input("Enter all the values:")
valuesList = values.split()
print(valuesList)
count = 0
for l in valuesList:
    if (int(l) < int(numK) ):
        count = count+1

print("Number of elements less than numK are:" + str(count))

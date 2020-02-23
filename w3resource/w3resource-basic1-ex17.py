number = int(input("Enter number:"))
difference = abs(number - 1000)

if (abs(number - 1000) <= 100):
    print("Number is within 100 of 1000")
elif (abs(number - 2000) <= 100):
    print("Number is within 100 of 2000")
else:
    print("Number is neither within 100 of either 1000 or 2000")
    
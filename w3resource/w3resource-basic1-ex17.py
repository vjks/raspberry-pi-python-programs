number = int(input("Enter number:"))

if number >= 100 and number <= 1000:
    print("Number is less than 1000")
elif number >= 1000 and number <= 2000:
    print("Number is > 1000 and < 2000")
else:
    print("Number < 100 or < 2000")
    
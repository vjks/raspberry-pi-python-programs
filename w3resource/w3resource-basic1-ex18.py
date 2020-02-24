number1 = int(input("Enter first number:"))
number2 = int(input("Enter second number:"))
number3 = int(input("Enter third number:"))

def sumofthree(number1, number2, number3):
    sum = number1 + number2 + number3
    if number1 == number2 == number3:
        sum = 3 * sum
    return sum
    
print(sumofthree(number1, number2, number3))
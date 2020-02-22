number = int(input("Enter number: "))
secondNumber = 17

def calculateDifference( number, secondNumber): 
    if number > secondNumber:
        return 2 * abs(number - secondNumber)
    else:
        return number - secondNumber

difference = calculateDifference(number, secondNumber)
print("Difference is: ", difference)
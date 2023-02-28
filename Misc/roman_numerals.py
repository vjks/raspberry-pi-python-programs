import re

def single_roman_numeral(num):
    match num:
        case 'I':
            return 1
        case 'II':
            return 2
        case 'III':
            return 3
        case 'IV':
            return 4
        case 'V':
            return 5
        case 'VI':
            return 6
        case 'VII':
            return 7
        case 'VIII':
            return 8
        case 'IX':
            return 9
        case 'X':
            return 10
        case 'XI':
            return 11
        case 'L':
            return 50
        case 'C':
            return 100
        case 'D':
            return 500
        case 'M':
            return 1000
        case default:
            return "something"

def calculate_roman_numeral(roman_numeral):
    roman_numeral = roman_numeral.upper()
    print("The provided roman numeral is: ", roman_numeral)
    strlen = len(roman_numeral)

    sum = 0
    previous = 0

    error1 = input_error(roman_numeral)
    error2 = vld_error(roman_numeral)
    
    while not error1 and not error2 and strlen > 0: 
        single_char = roman_numeral[0:1]
        value = single_roman_numeral(single_char)
        if previous > 0 and value > previous:
            sum = sum + (value - 2 * previous) # Previous needs to be subtracted twice
            print("sum, value and previous values are: ", sum, value, previous)
            previous = value
        else:
            sum += value
            previous = value
        
        roman_numeral = roman_numeral[1:]
        strlen = len(roman_numeral)
    
    if error1: 
        print("Error with input. Same character cannot be repeated more than three times in a row. ")
    elif error2:
        print("V, L, D cannot be repeated")
    else:
        print("Total sum is: ", sum)

def input_error(roman_numeral):
    occurence = re.findall(r"(\w)\1{3,}", roman_numeral)
    if len(occurence) > 0:
        return True
    else:
        return False

def vld_error(roman_numeral):
    occurence = re.findall(r"(V|L|D)\1{1,}", roman_numeral)
    if len(occurence) > 0:
        return True
    else:
        return False


print("Enter a roman numeral:")
roman_numeral = input().upper()
print("The entered roman numeral is: " + roman_numeral)
calculate_roman_numeral(roman_numeral)
calculate_roman_numeral("XI")
calculate_roman_numeral("XIV")
calculate_roman_numeral("XXV")
calculate_roman_numeral("XXX")
calculate_roman_numeral("XXXX")
calculate_roman_numeral("XV")
calculate_roman_numeral("XVVX")
calculate_roman_numeral("LXXXI")
calculate_roman_numeral("XCIX")
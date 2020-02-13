try:
    n = input("Enter n: ")
    print("Calculated result is: ", int(n) + int(n + n) + int(n + n + n));
except:
    print("Error. Entered value was probably not numeric and couldn't be cast into int")
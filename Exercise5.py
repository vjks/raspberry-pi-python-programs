celcius = input("Enter temperature in celcius: ")

# after replacing . with nothing is what's left behind numeric?
if celcius.replace('.', '', 1).isdigit() or celcius.isnumeric():  
    fahrenheit = (float(celcius) * (9/5)) + 32
    print("Temperature in fahrenheit is: " + str(fahrenheit) )
else:
    print("Please enter a numeric value.")
function = input("Enter the function: ")
function = function.replace("(", "")
function = function.replace(")", "")
print(type(function))
print(abs.__doc__) # Not sure how a function name can be added here through a string.
                   # If I put a string containing the function name. It just shows the doc for str.
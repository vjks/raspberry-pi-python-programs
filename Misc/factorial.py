def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i 
        #print("i is, result is", str(i), str(result))
    return result

print(factorial(4)) # should return 24
print(factorial(5)) 
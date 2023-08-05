a = int(input())
b = int(input())
c = input()

result = 0

if c == '+':
    result = a + b
elif c == '-':
    result = a - b
elif c == '/':
    result = a / b
elif c == '*':
    result = a * b

print(result)
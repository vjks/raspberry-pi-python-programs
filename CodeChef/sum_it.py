num_tests = int(input())

for x in range(num_tests):
    numbers = input().split()
    a = int(numbers[0])
    b = int(numbers[1])
    c = int(numbers[2])
    if a + b == c: 
        print("YES")
    else:
        print("NO")
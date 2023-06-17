tests = int(input())

for _ in range(tests):
    array_length = int(input())
    array_integer = list(map(int, input().split()))
    
    count = 0
    minimum = array_integer[0]
    for x in range(array_length):
        if array_integer[x] < minimum:
            minimum = array_integer[x]
    for index, item in enumerate(array_integer):
        if item > minimum:
            array_integer[index] = minimum
            count += 1
    print(count)
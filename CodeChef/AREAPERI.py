length = int(input())
breadth = int(input())

area = length * breadth
perimeter = 2 * (length + breadth)

if area > perimeter: 
    print("Area")
    print(area)
elif perimeter > area:
    print("Peri")
    print(perimeter)
else:
    print("Eq")
    print(area)
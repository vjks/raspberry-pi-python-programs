t = int(input())

for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    
    swap = 0
    previous = array[0]
    for _ in range(n - 1):
        if array[_] > array[_ + 1]:
            temp = array[_ + 1]
            array[_ + 1] = array[_]
            array[_] = temp
            break
    #print(array)
    for _ in range(n - 1):
        if array[_] > array[_ + 1]: 
            swap += 1
            break
    if swap > 0:
        print("NO")
    else:
        print("YES")
        
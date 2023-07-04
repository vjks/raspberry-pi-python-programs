import statistics
from statistics import mode
 
def most_common(List):
    return(mode(List))
   

t = int(input())

for _ in range(t):
    array_size = int(input())
    array = list(map(int, input().split()))
    
    element = most_common(array)
    count = 0
    for _ in array:
        if _ != element:
            count += 1
    print(count)

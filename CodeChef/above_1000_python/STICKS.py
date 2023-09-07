t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    if n > 3:
        # if the number of stick is greater than 4 we can form a rectangle.
        a.sort()
        side_a = side_b = 0
        
        # if the number of values is odd, if the first is not equal to second remove the first
        # else remove the second
        if n % 2 != 0:
            if a[0] != a[1]:
                a.pop(0)
            else:
                a.pop(n - 1)
            n -= 1
        
        
        i = n - 1   # The starting index of the list will be one less than the total number of values.
        
        # If the last value is equal to the 2nd last value and the 3rd last value is equal to the 4th last value
        # then assign the last value as one side and the 3rd last value as the other side.
        while(i > 0):
            if a[i] == a[i - 1]:
                if side_a == 0:
                    side_a = a[i]
                    i -= 2 # Found a matching pair, we need to skip two sticks, this one and the next one
                else:
                    side_b = a[i]
                    break # Since we found the next pair, we can just break the loop
            else:
                i -= 1 # Reduce to iterator by 1 so that we can check the next pair
            
        # if neither of the sides are 0 then print their product because that's the area.
        if side_a > 0 and side_b > 0:
            print(side_a * side_b)
        else:
            print(-1)
    else:
        print(-1)
num_tests = int(input())

for x in range(num_tests):
    str_length = int(input())
    given_str = input()
    counter = 0
    for x in given_str:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            counter = 0
            #print(counter)
        else:
            counter = counter + 1
            #print(counter)
            if counter >= 4:
                break;
    if counter >= 4:
        print("NO")
    else: 
        print("YES")
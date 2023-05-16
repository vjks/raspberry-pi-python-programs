num_tests = int(input())

for x in range(num_tests):
    a_age, b_age, c_age = map(int, input().split())
    perfect = False
    if a_age == (b_age + c_age) or b_age == (a_age + c_age) or c_age == (a_age + b_age):
        perfect = True
        
    if perfect:
        print("YES")
    else: 
        print("NO")
# This is my implmentation of the Eucledian algorithm.

tests = int(input())

for x in range(tests):
    a, b = map(int, input().split())
    prod_a_b = a * b # partial lcm calculation
    gcd = "error"
    while(b != 0):
        if b > a:
            c = a
            a = b
            b = c
        remainder = a % b
        if b == 0:
            gcd = a
            print(a, b, gcd)
        else:
            a = b
            b = remainder
            gcd = a # if b is 0 and the loop stops here then the gcd is a
    
    lcm = prod_a_b // gcd   
    print(gcd, lcm)
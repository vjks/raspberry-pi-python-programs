import re

t = int(input())

for _ in range(t):
    s = input()
    
    valid = "YES"
    # lower case characters should be present
    x = re.search("[a-z]", s)
    if not x:
        valid = "NO"
    
    #number of characters is more than 9
    if len(s) < 10:
        valid = "NO"
    
    # At least one digit must be strictly inside all the other characters
    y = re.search(".+[0-9].+", s)
    if not y:
        valid = "NO"
    
    # Must have one uppercase character strictly inside
    z = re.search(".+[A-Z].+", s)
    if not z:
        valid = "NO"
    
    # Must have one of the given special characters, strictly inside
    a = re.search(".+[@#%&?].+", s)
    if not a:
        valid = "NO"
    
    print(valid)
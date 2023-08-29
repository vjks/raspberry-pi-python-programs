import re

for _ in range(int(input())):
    string = input()
    
    x = re.search("010", string)
    y = re.search("101", string)
    
    if x or y:
        print("Good")
    else:
        print("Bad")
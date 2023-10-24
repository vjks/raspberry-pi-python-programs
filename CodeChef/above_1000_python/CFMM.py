t = int(input())

for _ in range(t):
    n = int(input())
    
    d = dict()
    for _ in range(n):
        s = input()
        meal = "codechef"
        # use a dictionary to count all the characters
        for _ in range(len(s)):
            if s[_] in meal:
                if s[_] in d:
                    d[s[_]] += 1
                else:
                    d[s[_]] = 1
    # iterate through the dictionary to find how many times all the characters of codechef appear.
    if len(d.values()) == 6:
        d['c'] = d['c'] // 2
        d['e'] = d['e'] // 2    
        print(min(d.values()))
    else:
        print(0)
string = 'X-DSPAM-Confidence: 0.8475 '

atpos = string.find(':')
print(atpos)
subString = string[atpos+1:]
print(subString, type(subString) )
subString = float(subString)
print(subString, type(subString))


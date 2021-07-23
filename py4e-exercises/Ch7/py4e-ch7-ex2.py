fname = input('Enter the file name: ')
try:
    fhandle = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

count = 0
total = 0
for line in fhandle:
    if line.startswith('X-DSPAM-Confidence:'):
        #print(line.rstrip())
        value = line[19:26]
        #print(float(value))
        count = count + 1
        total = total + float(value)

avg = total / count
print( 'count is: ' + str( count ), 'Average spam confidence: ' + str( avg ) )
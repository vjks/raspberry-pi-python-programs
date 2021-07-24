fname = input('Enter the file name: ')
if fname == "na na boo boo":
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    exit()
try:
    fhandle = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
    
count = 0
total = 0
for line in fhandle:
    if line.startswith('Subject:'):
        #print(line.rstrip())
        count = count + 1
print( 'There were ' + str(count), 'subject lines in ' + fname )

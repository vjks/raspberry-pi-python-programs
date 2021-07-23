fname = input('Enter the file name: ')
try:
    fhandle = open(fname)
    for line in fhandle:
        print(line.upper())
except:
    print('File cannot be opened:', fname)
    exit()
x = int( input("Enter a number:") )
f = open("tables.txt", "a")
for j in range( 2, x + 1 ):
    for i in range( 10 ):
        i = i + 1
        print( j, " * ", i, " = ", j * i)
        f.write( str(j) + " * " + str(i) + " = " + str(j * i) + '\n' )
    f.write('\n') # Add an extra line at the end of a table to improve readability.
f.close()

maxNum = 0
minNum = 0
num = "start"
numList = []

while num != "done":
    try:
        num = input("Enter a number:")
        num = int( num )
        numList.append( num )
    except:
        if( num != "done" ):
            print("Invalid input")
            
print( 'Maximum:', max( numList ) )
print( 'Mininum:', min( numList ) )


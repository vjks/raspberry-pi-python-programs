test_cases = int(input())

for x in range( test_cases ): 
    weeks_cost = input().split()
    print( int(weeks_cost[0]) * int(weeks_cost[1]) )
    
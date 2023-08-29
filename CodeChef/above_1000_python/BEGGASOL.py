t = int(input())

for _ in range(t):
    n = int(input())
    f = list(map(int, input().split()))
    
    gas = f[0] # The amount of gas in the car before it starts driving
    km = f[0] # The distance it can travel is equal to the units of fuel initially
    for _ in range(1, n):
        if gas == 0: # If we don't have any more guess after this we stop
            break
        km += f[_] # distance travelled is equal to the new gas stolen
        gas += f[_] # Steal gas from the next car while passing it
        gas -= 1 # The amount of gas will reduce by 1 unit while travelling

    print(km)
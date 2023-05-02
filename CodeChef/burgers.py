num_cases = int(input())

for x in range(num_cases):
    patty_and_bun = input().split()
    patty = int(patty_and_bun[0])
    bun = int(patty_and_bun[1])
    if patty < bun: 
        print(patty)
    elif bun < patty:
        print(bun)
    else:
        print(patty)
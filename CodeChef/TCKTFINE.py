num_tests = int(input())

for x in range(num_tests):
    fee, passengers, tickets = map(int, input().split())
    print((passengers - tickets) * fee)
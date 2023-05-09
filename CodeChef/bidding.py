num_tests = int(input())

for x in range(num_tests):
    (alice_bids, bob_bids, charlie_bids) = map(int, input().split() )
    all_bids = []
    all_bids.append(alice_bids)
    all_bids.append(bob_bids)
    all_bids.append(charlie_bids)
    all_bids.sort()
    
    if alice_bids == all_bids[2]:
        print("Alice")
    elif bob_bids == all_bids[2]:
        print("Bob")
    else:
        print("Charlie")
t = int(input())

for _ in range(t):
    a1, a2, a3, b1, b2, b3 = map(int, input().split())
    
    alice_total = [a1, a2, a3]
    bob_total = [b1, b2, b3]
    
    alice_total.sort(reverse = True)
    alice_total_str = str(alice_total[0]) + str(alice_total[1]) + str(alice_total[2])

    
    bob_total.sort(reverse = True)
    bob_total_str = str(bob_total[0]) + str(bob_total[1]) + str(bob_total[2])

    
    if int(alice_total_str) > int(bob_total_str):
        print("Alice")
    elif int(bob_total_str) > int(alice_total_str):
        print("Bob")
    else:
        print("Tie")
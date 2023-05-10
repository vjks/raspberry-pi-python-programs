num_tests = int(input())

for x in range(num_tests):
    total_chocolates = input().split()
    num_chocolates_alice = int(total_chocolates[0])
    bob_num_chocolates = int(total_chocolates[1])
    if (num_chocolates_alice + bob_num_chocolates) % 2 == 0:
        print("YES")
    else:
        print("NO")
num_tests = int(input())

for x in range(num_tests):
    amounts = input().split()
    amount_brought = int(amounts[0])
    amount_needed = int(amounts[1])
    if amount_needed <= amount_brought:
        print("YES")
    else:
        print("NO")

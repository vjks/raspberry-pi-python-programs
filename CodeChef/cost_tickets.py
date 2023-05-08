num_tests = int(input())
max_ticket_value = 1000

for x in range(num_tests):
    cost_of_ticket = int(input())
    if cost_of_ticket * 4 > max_ticket_value:
        print("NO")
    else:
        print("YES")
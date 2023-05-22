tests = int(input())

for x in range(tests):
    amount_spent = int(input())
    discount = 0
    if(amount_spent <= 100):
        discount = 0
    elif amount_spent > 100 and amount_spent <= 1000:
        discount = 25
    elif amount_spent > 1000 and amount_spent <= 5000:
        discount = 100
    elif amount_spent > 5000:
        discount = 500
    print(amount_spent - discount)
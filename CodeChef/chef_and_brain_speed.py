bit_rates = input().split()
limit = int(bit_rates[0])
chefs_rate = int(bit_rates[1])

if chefs_rate <= limit:
    print("NO")
else:
    print("YES")
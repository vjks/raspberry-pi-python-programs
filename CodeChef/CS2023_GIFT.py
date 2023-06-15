has_amount, laptop_price, fund_amount = map(int, input().split())
    
if has_amount + fund_amount >= laptop_price:
    print("YES")
else:
    print("NO")
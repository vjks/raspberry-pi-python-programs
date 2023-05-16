tests = int(input())

for x in range(tests):
    a_model, b_model, discount_a, discount_b = map(int, input().split())
    a_model_price = a_model - discount_a
    b_model_price = b_model - discount_b
    if a_model_price < b_model_price:
        print("FIRST")
    elif b_model_price < a_model_price:
        print("SECOND")
    else:
        print("ANY")
    
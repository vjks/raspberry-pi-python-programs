tests = int(input())

for _ in range(tests):
    chef_floor, chefina_floor, chef_rate, chefina_rate = map(int, input().split())
    
    if chef_floor / chef_rate < chefina_floor / chefina_rate:
        print("chef")
    elif chef_floor / chef_rate > chefina_floor / chefina_rate:
        print("chefina")
    else:
        print("Both")
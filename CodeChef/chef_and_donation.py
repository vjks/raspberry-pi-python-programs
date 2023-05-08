num_tests = int(input())
    
for x in range(num_tests):
    incomes = input().split()
    chefs_income = int(incomes[0])
    chefinas_income = int(incomes[1])
    print(chefinas_income - chefs_income)
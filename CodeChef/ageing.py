chef_age = 20 
chefina_age = 10

num_tests = int(input())

for x in range(num_tests):
    future_age_chef = int(input())
    extra_years = future_age_chef - chef_age
    print( chefina_age + extra_years )

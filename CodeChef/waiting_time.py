num_tests = int(input())

for x in range(num_tests):
    weeks_and_days = input().split()
    days_passed = int(weeks_and_days[1])
    num_weeks = int(weeks_and_days[0])
    print((num_weeks * 7 )- days_passed)
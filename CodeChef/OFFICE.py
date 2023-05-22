tests = int(input())

for x in range(tests):
    mon_thu_hours, fri_hours = map(int, input().split())
    print(mon_thu_hours * 4 + fri_hours)
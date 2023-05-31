tests = int(input())

for x in range(tests):
    police_location, thief_location = map(int, input().split())
    print(abs(police_location - thief_location))
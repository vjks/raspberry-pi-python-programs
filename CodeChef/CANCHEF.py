num_tests = int(input())

for x in range(num_tests):
    petrol, distance = map(int, input().split())
    if distance * 2 <= petrol * 15:
        print("YES")
    else:
        print("NO")
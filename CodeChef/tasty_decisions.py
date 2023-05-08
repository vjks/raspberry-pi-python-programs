num_tests = int(input())

for x in range(num_tests):
    tastiness = input().split()
    chocolate_tastiness =  int(tastiness[0])
    candy_tastiness = int(tastiness[1])
    if 2 * chocolate_tastiness > 5 * candy_tastiness:
        print("Chocolate")
    elif 2 * chocolate_tastiness < 5 * candy_tastiness:
        print("Candy")
    else:
        print("Either")
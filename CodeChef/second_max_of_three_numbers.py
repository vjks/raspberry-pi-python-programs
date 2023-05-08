num_triples = int(input())

for x in range(num_triples):
    three_nums = input().split()
    numerical_list = []
    for y in three_nums:
        numerical_list.append(int(y))
    numerical_list.sort()
    print(numerical_list[1] )
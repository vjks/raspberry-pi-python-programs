tests = int(input())

for x in range(tests):
    num_problems = int(input())
    remove_count = 0
    ratings = input().split()
    for rating in ratings:
        if int(rating) >= 1000:
            remove_count = remove_count + 1
    print(remove_count)
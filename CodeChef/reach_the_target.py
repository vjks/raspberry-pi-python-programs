num_tests = int(input())

for x in range(num_tests):
    scores = input().split()
    target = int(scores[0])
    current_score = int(scores[1])
    print(target - current_score)
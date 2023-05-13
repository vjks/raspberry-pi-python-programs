num_tests = int(input())

for x in range(num_tests):
    num_questions, alice_score = map(int, input().split())
    print(num_questions - alice_score)
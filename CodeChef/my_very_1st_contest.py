users = input().split()

new = int(users[0])
not_submitted = int(users[1])
submitted_not_solved = int(users[2])

rated = new - not_submitted
rating_1000 = new - (not_submitted + submitted_not_solved)
print(submitted_not_solved + rating_1000, rating_1000)
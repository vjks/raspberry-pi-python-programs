t = int(input())

for _ in range(t):
    string = input()
    brass_count = amber_count = 0
    for _ in string:
        if _ == 'a':
            brass_count += 1
        else:
            amber_count += 1
    print(min(brass_count, amber_count))
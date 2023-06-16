parent1, parent2 = map(str, input().split())

if parent1 == 'R' and parent2 == 'R':
    print('R')
elif parent1 == 'B' and parent2 == 'B':
    print('B')
elif parent1 == 'G' and parent2 == 'G':
    print('G')
elif parent1 == 'G' and parent2 == 'B':
    print('B')
else:
    print('R')
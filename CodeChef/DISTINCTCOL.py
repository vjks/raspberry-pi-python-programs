tests = int(input())

for _ in range(tests):
    num_colors = int(input())
    balls = map(int, input().split())
    print(max(balls))
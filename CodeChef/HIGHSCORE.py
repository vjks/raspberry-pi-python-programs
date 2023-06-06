tests = int(input())

for _ in range(tests):
    num_problems = int(input())
    na, nb, nc, nd = map(int, input().split())
    max_a_b = max(na, nb)
    max_c_d = max(nc, nd)
    print(max(max_a_b, max_c_d))
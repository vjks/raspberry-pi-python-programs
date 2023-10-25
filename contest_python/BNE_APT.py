n, m = map(int, input().split())
x, y = map(int, input().split())

bones_total = n * x
blood_total = m * y

print(bones_total + blood_total)
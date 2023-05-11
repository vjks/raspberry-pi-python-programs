num_tests = int(input())

for x in range(num_tests):
    pages_read_days = input().split()
    num_pages = int(pages_read_days[0])
    pages_read = int(pages_read_days[1])
    days = int(pages_read_days[2])
    if num_pages <= pages_read * days:
        print("YES")
    else:
        print("NO")
    
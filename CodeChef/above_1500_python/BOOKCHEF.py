n, m = map(int, input().split())
a = list(map(int, input().split()))

special_list = list()
other_list = list()
content = list()
for _ in range(m):
    line = list(input().split())
    f = int(line[0])
    p = int(line[1])
    s = line[2]
    if f in a:
        special_list.append((f, p, s))
    else:
        other_list.append((f, p, s))

special_list.sort(key=lambda x:x[1], reverse = True)
other_list.sort(key=lambda x:x[1], reverse = True)

for content in special_list:
    print(content[2])

for content in other_list:
    print(content[2])

tests = int(input())

for x in range(tests):
    to_generate, num_years, grams_he3, he3_power = map(int, input().split())
    if grams_he3 * he3_power >= to_generate * num_years:
        print("YES")
    else:
        print("NO")
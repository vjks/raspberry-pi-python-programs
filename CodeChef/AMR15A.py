soldiers_num = int(input())

odd_weapons = 0
even_weapons = 0
weapons = map(int, input().split())
for y in weapons:
    if int(y) % 2 == 0:
        even_weapons = even_weapons + 1 
    else:
        odd_weapons = odd_weapons + 1
if even_weapons > odd_weapons:
    print("READY FOR BATTLE")
else:
    print("NOT READY")

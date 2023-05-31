tests = int(input())

for _ in range(tests):
    total_cards, faceup_cards = map(int, input().split())
    if(faceup_cards == 0): 
        print(0)
    elif faceup_cards == total_cards:
        print(0)
    elif faceup_cards > (total_cards / 2):
        print(total_cards - faceup_cards)
    else:
        print(faceup_cards)
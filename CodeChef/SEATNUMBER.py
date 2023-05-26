tests = int(input())

for x in range(tests):
    seat_number = int(input())
    seat_type = ""
    if seat_number >= 1 and seat_number <= 10:
        seat_type = seat_type + "Lower Double"
    elif seat_number >= 11 and seat_number <= 15:
        seat_type = seat_type + "Lower Single"
    elif seat_number >= 15 and seat_number <= 25:
        seat_type = seat_type + "Upper Double"
    elif seat_number >= 26 and seat_number <= 30:
        seat_type = seat_type + "Upper Single"
    else:
        seat_type = "ERROR"
    print(seat_type)
hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
regularHours = 40
overtimeRate = 1.5

if hours > regularHours:
    overtime = hours - regularHours
    overtimePay = overtime * rate * overtimeRate
    regularPay = regularHours * rate
    print("Pay: " + str( overtimePay + regularPay ) )
else:
    print("Pay: " + str( int(hours) * float(rate) ) )
import datetime

firstDateList = input("Enter start date YYYY,MM,DD: ").split(",")
secondDateList = input("Enter end date YYYY,MM,DD: ").split(",")

#first= firstDate.split(",")
#= secondDate.split(",")

firstDate = datetime.date(int(firstDateList[0]), int(firstDateList[1]), int(firstDateList[-1]))
secondDate = datetime.date(int(secondDateList[0]), int(secondDateList[1]), int(secondDateList[-1]))
print((secondDate - firstDate).days)
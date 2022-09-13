import datetime
import time

def get_IST(unix_timestamp, ctd_seconds):
    second_country_unix_time = unix_timestamp + ctd_seconds
    date_time = datetime.datetime.fromtimestamp(second_country_unix_time).strftime("%H:%M:%S")
    print("The current time in India is: " + str(date_time))

def get_EST(unix_timestamp, ctd_seconds):
    second_country_unix_time = unix_timestamp - ctd_seconds
    date_time = datetime.datetime.fromtimestamp(second_country_unix_time).strftime("%H:%M:%S")
    print("The current Eastern Standard Time is: " + str(date_time))

def is_daylight_Savings(unix_timestamp):
    day_of_the_year = datetime.datetime.fromtimestamp(unix_timestamp).strftime("%j")
    print("Today's day is:" + str(day_of_the_year))
    date_numeral = datetime.datetime.today().weekday()
    options = {
        0 : "Monday",
        1 : "Tuesday",
        2 : "Wednesday",
        3 : "Thursday",
        4 : "Friday",
        5 : "Saturday",
        6 : "Sunday",
    }
    print(options.get(date_numeral))
    if int(day_of_the_year) > 71 and int(day_of_the_year) < 311:
        now = datetime.datetime.now()
        today2am = now.replace(hour=2, minute=0, second=0, microsecond=0)
        if now > today2am:
            return True
    else:
        return False


unix_timestamp = time.time()

try:
    current_location = input("Enter the country you are in:")
    if is_daylight_Savings(unix_timestamp):
        ctd_seconds =  9.5 * 60 * 60
    else:
        ctd_seconds = 10.5 * 60 * 60
    if current_location.lower() == "india":
        get_EST(unix_timestamp, ctd_seconds)
    elif current_location.lower() == "canada":
        get_IST(unix_timestamp, ctd_seconds)
    else:
        print("Incorrect input")
except ValueError:
    print("Incorrect input. Please check your input.")
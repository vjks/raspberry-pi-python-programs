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

unix_timestamp = time.time()

try:
    current_time_difference = float(input("Enter current time difference as a decimal value:"))
    current_location = input("Enter the country you are in:")
    ctd_seconds =  current_time_difference * 60 * 60
    if current_location.lower() == "india":
        get_EST(unix_timestamp, ctd_seconds)
    elif current_location.lower() == "canada":
        get_IST(unix_timestamp, ctd_seconds)
    else:
        print("Incorrect input")
except ValueError:
    print("Incorrect input. Please check your input.")
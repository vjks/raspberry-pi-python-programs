import re
def check_time(text):
 # pattern = "[1-12]:[00-59]\s*[AM|PM|am|pm]"
#pattern = "[0-9]:[0-5][0-9]\s*AM|am|pm|PM"
  pattern = "[0-9]*[0-9]:[0-5][0-9]\s*(AM|am|pm|PM)"
  result = re.search(pattern, text,)
  return result
    
print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
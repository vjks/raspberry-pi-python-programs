#!/usr/bin/env python3
import re
import operator
import csv

error = {}
per_user = {}

with open("syslog.log") as file:
    for line in file:
        #result = re.search(r"ticky: ERROR ([\w ]*).*$", line)
        result = re.search(r"ticky: ERROR (([\w ]*).*) ", line)
        #result = re.search(r"ticky: ERROR", line)
        if result is not None:
            error_msg = result.group(1)
            #print( error_msg )
            if error_msg not in error.keys():
                error[error_msg] = 1
            else:
                error[error_msg] += 1
        #else:
        #    print(result)
        
        result = re.search(r"ticky: (ERROR|INFO) ([\w ]*).*\((\w*)\)*$", line)
        if result is not None:
            type = result.group(1)
            print("Error/Info type is: " + type)
            username = result.group(3)
            if username not in per_user.keys():
                per_user[username] = {
                    "INFO": 0,
                    "ERROR": 0
                }
                #per_user[username] = {}
                #per_user[username]["INFO"] = 0
                #per_user[username]["ERROR"] = 0
            else:
                per_user[username][type] += 1
#print(error)
per_user = sorted(per_user.items(), key=operator.itemgetter(0))
error = sorted(error.items(), key=operator.itemgetter(1), reverse=True)

error.insert(0, ('Error', 'Count'))
#per_user.insert(0, ("Username", "INFO", "ERROR"))

print(per_user)
print(error)

#for user_value in per_user.values():
 #       print(user_value)

filename = "error_message.csv"
user_fileName = "user_statistics.csv"



def write_to_files(filename, filename2):
    with open('error_message.csv', 'w', newline='') as f:
        # create the csv writer
        writer = csv.writer(f)

        # write a row to the csv
        for row in error:  
            writer.writerow(row)
    with open('user_statistics.csv', 'w') as f:
        f.write("Username,INFO,ERROR\n")

    with open('user_statistics.csv', 'a') as f:
        # create the csv writer
        for myrow in per_user:
            #line = json.loads(myrow[1])
            to_write = ""
            f.write(to_write)
            to_write += myrow[0] + ","
            values = ""
            for value in myrow[1].values():
                values +=  str(value) + ','
            to_write += values[:-1]
            f.write(to_write + "\n")

write_to_files(filename, user_fileName)
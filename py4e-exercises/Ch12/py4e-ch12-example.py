import socket, re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
header = True
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    data = data.decode()

    if re.search('[HTTP/].*\r\n\r\n', data): # if data starts from HTTP and contains any number of characters followed by two consecutive next line characters ...
        pos = data.find('\r\n\r\n') # Find where the two consecutive next line characters start from
        data = data[pos+4:] # Data to be printed starts from 4 characters after the first carriage return
        print(data, end='') # Print the data
    else:
        print(data, end='') # if the data doesn't two consecutive
mysock.close()
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#url = input('Enter URL: ')

#hostname = url.split("/")
mysock.connect(('aoghs.org', 80))
cmd = 'GET https://aoghs.org/technology/oil-well-pump/ HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

try:
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()
except:
    print("An exception occured. Check URL, perhaps?")
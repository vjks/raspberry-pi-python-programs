import urllib.request, urllib.parse, urllib.error

img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
#fhand = open('cover3.jpg', 'wb')
size = 0
while True:
    info = img.read(1)
    if len(info) < 1: break
    size = size + len(info)
    if size <= 3000:
        print(info.decode(),end='')

print(size, 'characters copied.')
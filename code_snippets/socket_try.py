import socket
url = input("Enter a URL: ")

words = url.split("/")
host = words[2]
print(host)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = 'GET '+url+'HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())

mysock.close()
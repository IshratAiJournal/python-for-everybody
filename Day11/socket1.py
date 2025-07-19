import socket

# Step 1: Create a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Connect to the server
mysock.connect(('data.pr4e.org', 80))

# Step 3: Prepare the GET request
cmd = 'GET /intro-short.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()

# Step 4: Send the request
mysock.send(cmd)

# Step 5: Receive the response
response = b''
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    response += data

mysock.close()

# Step 6: Split headers and body
header_end = response.find(b'\r\n\r\n')
headers = response[:header_end].decode()
body = response[header_end+4:]

# Step 7: Print the first word of the file
first_word = body[:100].decode(errors='ignore').split()[0]
print('✅ First word of the file is:', first_word)

# Step 8: Print ETag and Content-Length
for line in headers.split('\r\n'):
    if 'ETag' in line or 'Content-Length' in line:
        print('📄', line)

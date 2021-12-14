from sys import argv


text = argv[1]

for t in text.split():
    if ":" in t: continue
    t = t.strip().replace("0x", "")
    c = ["0x"+i+j for i,j in zip(t[::2], t[1::2])]
    c.reverse()
    c = [x.replace('0x00','0x3d') for x in c]
    print(*c, end=' ')
print()
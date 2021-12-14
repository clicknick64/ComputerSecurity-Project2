import hashlib
import base64

word = "834472"

m = hashlib.sha256()
m.update(word.encode())
sha = word + ":" + m.hexdigest()
base = base64.b64encode(sha.encode())
print(base.decode())
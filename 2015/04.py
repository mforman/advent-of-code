import hashlib

salt = "yzbqklnj"
i = 1
while True:
    plain = salt + str(i)
    enc = bytes(plain, "utf-8")
    m = hashlib.md5(enc).hexdigest()
    if m[0:6] == "000000":
        break
    i += 1

print(i)
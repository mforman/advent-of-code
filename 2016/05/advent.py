import hashlib

print('Advent problem #5')

door_id = 'ojvtpuvg'
x = 0
length = 0

pwd = []
for i in range(8):
    pwd.append('')

while length < 8:
    s = door_id + str(x)
    hash = hashlib.md5(s.encode('utf-8'))
    h = hash.hexdigest()
    if str.startswith(h, '00000'):
        ordinal = int(h[5], 16)
        if ordinal < 8 and pwd[ordinal] == '':
            val = h[6]
            print('Found {} for position {}'.format(val, ordinal))
            pwd[ordinal] = val
            length += 1
    x += 1

print(''.join(pwd))

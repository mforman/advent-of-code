def transform(sub, start=0, seed=1, end=None):
    val = seed
    loop_size = start + 1
    while True:
        val = (val * sub) % 20201227
        yield (loop_size, val)
        if end and loop_size == end:
            break
        loop_size += 1


# card = 5764801
# door = 17807724

card = 335121
door = 363891

matches = {}
keys = set([card, door])

for loop_size, key in transform(7):
    if key in keys:
        matches[key] = loop_size
        keys.remove(key)
        print(f"{loop_size} - {key}")
    if len(keys) == 0:
        break

if matches[card] < matches[door]:
    loop = matches[card]
    key = door
else:
    loop = matches[door]
    key = card

enc = list(transform(key, end=loop))[-1][1]

print(enc)

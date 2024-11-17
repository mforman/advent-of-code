def is_aba(item):
    if len(item) != 3:
        return False
    if item[0] != item[2]:
        return False
    if item[0] == item[1]:
        return False
    return True


def flip_aba(item):
    return ''.join([item[1], item[0], item[1]]) 


def is_abba(item):
    if len(item) != 4:
        return False
    if item[0] != item[3]:
        return False
    if item[1] != item[2]:
        return False
    if item[0] == item[1]:
        return False
    return True


def supports_tls(item):
    in_hypernet = False
    is_valid = False

    for i in range(0, len(item) - 3):
        candidate = item[i:i+4]
        if candidate[0] == '[':
            in_hypernet = True
            continue
        if candidate[0] == ']':
            in_hypernet = False
            continue
        if any(c in candidate for c in ('[', ']')):
            continue

        if not is_abba(candidate):
            continue

        if in_hypernet:
            return False

        is_valid = True
    return is_valid


def supports_ssl(item):
    in_hypernet = False
    aba = []
    bab = []

    for i in range(0, len(item) - 2):
        candidate = item[i:i+3]
        if candidate[0] == '[':
            in_hypernet = True
            continue
        if candidate[0] == ']':
            in_hypernet = False
            continue
        if any(c in candidate for c in ('[', ']')):
            continue

        if not is_aba(candidate):
            continue

        if in_hypernet:
            bab.append(candidate)
        else:
            aba.append(candidate)

    if aba.count == 0 or bab.count == 0:
        return False

    for x in aba:
        if flip_aba(x) in bab:
            return True

    return False


with open('input.txt', 'r') as f:
    items = f.read().splitlines()

count = 0

for item in items:
    if supports_ssl(item):
        count += 1    
print(count)

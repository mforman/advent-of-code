def decompress(item, length_only=False):
    position = 0
    in_marker = False
    marker = []
    repeat_pending = False
    num_chars = 0
    num_repeat = 0
    decompressed = []
    raw_length = 0
    ret = {}

    while position < len(item):
        current = item[position]

        if repeat_pending:
            chars = item[position:position+num_chars]
            for i in range(0, num_repeat):
                if not length_only:
                    decompressed += chars
            repeat_pending = False
            position += num_chars
            raw_length += num_chars * num_repeat
            continue

        if current == '(':
            in_marker = True
            marker = []
            position += 1
            continue

        if current == ')':
            in_marker = False
            marker_str = ''.join(marker)
            marker_seg = marker_str.split('x')
            num_chars = int(marker_seg[0])
            num_repeat = int(marker_seg[1])
            repeat_pending = True
            position += 1
            continue

        if in_marker:
            marker.append(current)
            position += 1
            continue

        if not length_only:
            decompressed.append(current)
        raw_length += 1
        position += 1

    ret = {}
    ret['length'] = raw_length
    if not length_only:
        ret['value'] = ''.join(decompressed)
    
    return ret


def expanded_length(item):
    length = 0
    position = 0
    in_marker = False
    marker = []
    repeat_pending = False
    num_chars = 0
    num_repeat = 0

    while position < len(item):
        current = item[position]

        if repeat_pending:
            sub = item[position:position+num_chars]

            length += expanded_length(sub) * num_repeat

            repeat_pending = False
            position += num_chars
            continue

        if current == '(':
            in_marker = True
            marker = []
            position += 1
            continue

        if current == ')':
            in_marker = False
            marker_str = ''.join(marker)
            marker_seg = marker_str.split('x')
            num_chars = int(marker_seg[0])
            num_repeat = int(marker_seg[1])
            repeat_pending = True
            position += 1
            continue

        if in_marker:
            marker.append(current)
            position += 1
            continue

        length += 1
        position += 1
    return length

with open('input.txt', 'r') as f:
    compressed = f.read()

# compressed = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'

compressed = ''.join(compressed.split())

result = expanded_length(compressed)

print(result)

# result = decompress(compressed, False)

# print(result['length'])
# print(result['value'])

# result = decompress(result['value'], True)

# print(result['length'])
# print(result['value'])

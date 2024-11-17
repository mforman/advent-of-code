from collections import Counter

input = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'

with open('08.txt', 'r') as f:
    input = f.read()

license = [*map(int, input.split())]

nodes = []
part1 = 0

def parseNode(license):
    global part1
    childCount = license.pop(0)
    metaCount = license.pop(0)
    children = []
    meta = []
    while childCount > 0:
        child = parseNode(license)
        children.append(child)
        childCount -= 1
    while metaCount > 0:
        m = license.pop(0)
        part1 += m
        meta.append(m)
        metaCount -= 1
    return (meta, children)

def getTotal(node):
    meta, children = node
    total = 0
    if not children:
        total = sum(meta)
    else:
        for m in meta:
            i = m - 1
            if i < 0 or m > len(children):
                continue
            total += getTotal(children[i])
    return total 



nodes = parseNode(license)  

print ('Part 1: {}'.format(part1))
print ('Part 2: {}'.format(getTotal(nodes)))



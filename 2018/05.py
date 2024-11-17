from collections import Counter

#                  111111
#        0123456789012345
chain = 'dabAcCaCBAcCcaDA'

with open('05.txt', 'r') as f:
    chain = f.read().strip()

def isMatch(a, b):
    return abs(ord(a) - ord(b)) == 32

def react(chain):
    buf = []
    for c in chain:
        if buf and isMatch(c, buf[-1]):
            buf.pop()
        else:
            buf.append(c)
    return len(buf)
    

def solvePart2(chain):
    agents = set([c.lower() for c in chain])
    return min([react(chain.replace(a, '').replace(a.upper(), '')) 
                    for a in agents])

# def solvePart2(chain):
#     agents = set([c.lower() for c in chain])
#     results = {}
#     for a in agents:
#         stripped = strip(chain, a)
#         result = react(stripped)
#         results[a] = len(result)
    
#     cnt = Counter(results)
#     return cnt.most_common()[-1][1]

part1 = react(chain)
part2 = solvePart2(chain)
print('Part 1: {0}'.format(part1))
print('Part 2: {0}'.format(part2))

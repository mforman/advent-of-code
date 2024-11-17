def findTwoAndThrees(s):
    dictionary = {}
    for c in s:
        if c in dictionary:
            dictionary[c] += 1
        else:
            dictionary[c] = 1

    result = [0,0]

    for val in dictionary.values():
        if val == 2:
            result[0] = 1
        elif val == 3:
            result[1] = 1
    
    return result

def solvePart1(items):
    counter = [0,0]

    for item in items:
        result = findTwoAndThrees(item)
        counter[0] = counter[0] + result[0]
        counter[1] = counter[1] + result[1]

    return counter[0] * counter[1]   

def solvePart2(items):
    for item in items:
        for candidate in items:
            if item == candidate:
                continue
            
            differences = []

            for i in range(0, len(item)):
                if item[i] != candidate[i]:
                    differences.append(item[i])

            result = []
            if len(differences) == 1:
                for c in item:
                    if c not in differences:
                        result.append(c)
                return ''.join(result)

# items = [
#     'abcde',
#     'fghij',
#     'klmno',
#     'pqrst',
#     'fguij',
#     'axcye',
#     'wvxyz'
# ]

# items = [
#     'abcdef',
#     'bababc',
#     'abbcde',
#     'abcccd',
#     'aabcdd',
#     'abcdee',
#     'ababab'
# ]

with open('02.txt', 'r') as f:
    items = f.read().splitlines()

print ('Part 1: {0}'.format(solvePart1(items)))
print ('Part 2: {0}'.format(solvePart2(items)))


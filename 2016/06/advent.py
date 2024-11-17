print('Advent problem #6')

f = open('input.txt', 'r')

isFirstLine = True
letterCount = 0
map = []
result = []

for line in f:
    if isFirstLine:
        letterCount = len(line) - 1
        for i in range(letterCount):
            map.append({})
        print('The word is {} letters'.format(letterCount))
        isFirstLine = False
    # print(line, end='')
    for i in range(letterCount):
        count = 1
        letter = line[i]
        if letter in map[i]:
            count = map[i][letter] + 1
        map[i][letter] = count

for i in range(letterCount):
    letters = sorted(map[i].items(), key=lambda x: (x[1], x[0]))
    result.append(letters[0][0])
print(''.join(result))



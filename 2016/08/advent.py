class Screen(object):
    ON_PIXEL = '#'
    OFF_PIXEL = ' '

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = []
        for x in range(0, height):
            col = []
            for y in range(0, width):
                col.append(self.OFF_PIXEL)
            self.screen.append(col)


    def print(self):
        result = []
        for row in self.screen:
            result += row
            result.append('\n')
        print(''.join(result))


    def count_on(self):
        count = 0
        for row in self.screen:
            for col in row:
                if col == self.ON_PIXEL:
                    count += 1
        return count


    def rect(self, width, height):
        for x in range(0, height):
            for y in range(0, width):
                self.screen[x][y] = self.ON_PIXEL


    def rotate_column(self, x, by):
        original = []
        for i in range(0, self.height):
            original.append(self.screen[i][x])
        for i in range(0, self.height):
            source = i - by
            if source < 0:
                source += self.height
            self.screen[i][x] = original[source]

    def rotate_row(self, y, by):
        original = []
        for i in range(0, self.width):
            original.append(self.screen[y][i])
        for i in range(0, self.width):
            source = i - by
            if source < 0:
                source += self.width
            self.screen[y][i] = original[source]

def parse_line(line, screen):
    segments = line.split(' ')
    if segments[0] == 'rect':
        sub = segments[1].split('x')
        screen.rect(int(sub[0]), int(sub[1]))
    if segments[0] == 'rotate':
        cmd = segments[1]
        anchor = int(segments[2][2:])
        amount = int(segments[4])
        if cmd == 'row':
            method = screen.rotate_row
        if cmd == 'column':
            method = screen.rotate_column
        method(anchor, amount)


with open('input.txt', 'r') as f:
    items = f.read().splitlines()

screen = Screen(50, 6)

for i in items:
    parse_line(i, screen)
    #screen.print()

screen.print()
print('Number of ON piexls: {}'.format(screen.count_on()))


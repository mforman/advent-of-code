import array

class ChipTarget(object):
    def factory(type, id):
        if type == 'Bot': return Bot(id)
        if type == 'Output': return Output(id)
        assert 0, 'Unsupported type' + type
    factory = staticmethod(factory)

class Bot(ChipTarget):
    def __init__(self, id):
        self.id = int(id)
        self.chips = array.array('i')

    def __eq__(self, value):
        return self.id == value.id

    def add(self, value):
        self.chips.append(int(value))
        self.__execute()
    
    def add_low(self, value):
        self.low = value
        self.__execute()
    
    def add_high(self, value):
        self.high = value
        self.__execute()

    def __execute(self):
        if len(self.chips) != 2 or not hasattr(self, 'low') or not hasattr(self, 'high'):
            return
        self.chips = sorted(self.chips)
        if int(self.chips[0]) == 17 and int(self.chips[1]) == 61:
            print('Bot {} is comparing {} and {}'.format(self.id, self.chips[0], self.chips[1]))
        self.low(self.chips[0])
        self.high(self.chips[1])
        self.chips = []


class Output(ChipTarget):
    def __init__(self, id):
        self.id = int(id)
        self.value = None
        self.chips = array.array('i')


    def add(self, value):
        self.chips.append(int(value))


def get_or_create_item(items, type, id):
    if id in items:
        return items[id]
    item = ChipTarget.factory(type, id)
    items[id] = item
    return item


with open('input.txt', 'r') as f:
    instructions = f.readlines()

bots = {}
outputs = {}

for i in instructions:
    seg = i.strip().split(' ')
    if seg[0] == 'bot':
        # print('instruction: {}'.format(seg[1:]))
        bot = get_or_create_item(bots, 'Bot', seg[1])
        low = None
        high = None

        if seg[5] == 'bot':
            low = get_or_create_item(bots, 'Bot', seg[6])
        else:
            low = get_or_create_item(outputs, 'Output', seg[6])

        if seg[10] == 'bot':
            high = get_or_create_item(bots, 'Bot', seg[11])
        else:
            high = get_or_create_item(outputs, 'Output', seg[11])

        bot.add_low(low.add)
        bot.add_high(high.add)
    elif seg[0] == 'value':
        # print('assignment: {}'.format(seg[1:]))
        value = seg[1]
        bot = get_or_create_item(bots, 'Bot', seg[5])
        bot.add(value)

for k in sorted(outputs, key=lambda x: int(x)):
    print('Output {}: {}'.format(outputs[k].id, outputs[k].chips))
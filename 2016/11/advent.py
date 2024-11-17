#! /usr/bin/env python

import copy
import hashlib
from itertools import chain, repeat
from multiprocessing import Pool
import string
import sys

ELEMENTS = {}

class Component:
    def __init__(self, element):
        symbol = ELEMENTS[element.upper()]
        self.symbol = symbol

    def __lt__(self, value):
        return str(self) < str(value)

    def is_safe_with(self, b):
        if not isinstance(b, Component):
            return False
        if type(self) == type(b):
            return True
        if self.symbol == b.symbol:
            return True
        return False

    @staticmethod
    def are_all_safe(items):
        chips = []
        generators = []

        for item in items:
            if isinstance(item, Microchip):
                chips.append(item.symbol)
            elif isinstance(item, Generator):
                generators.append(item.symbol)
            else:
                raise 'Unknown type of object to check'

        for gen in generators:
            if gen in chips:
                chips.remove(gen)

        for chip in chips:
            unsafe = [g for g in generators if g != chip]
            if len(unsafe) > 0:
                return False
        return True


class Microchip(Component):
    def __init__(self, element):
        Component.__init__(self, element)

    def __str__(self):
        return '{}-M'.format(self.symbol)


class Generator(Component):
    def __init__(self, element):
        Component.__init__(self, element)

    def __str__(self):
        return '{}-G'.format(self.symbol)


class Elevator:
    def __init__(self):
        self.floor = 0
        self.components = []
        self.capacity = 2

    def __hash__(self):
        if len(self.components) > 0:
            fs = frozenset(self.components.sort(key=lambda x: str(x)))
        else:
            fs = frozenset(self.components)
        return hash((self.floor, fs))

    def open_slots(self):
        return self.capacity - len(self.components)

class Position:
    def __init__(self):
        self.floors = {}
        self.elevator = Elevator()

    def __hash__(self):
        digest = hashlib.md5(str(self).encode('utf-8')).hexdigest()
        return int(digest, 16)

    def __eq__(self, value):
        return hash(self) == hash(value)

    def __str__(self):
        all_items = []
        for k in self.floors:
            all_items += self.floors[k]

        all_items.sort(key=lambda x: str(x))

        result = ''
        for k in sorted(self.floors, reverse=True):
            result += 'F{}'.format(k+1)

            if self.elevator.floor == k:
                result += ' E '
            else:
                result += ' . '

            for item in all_items:
                result += ' '
                if item in self.floors[k]:
                    val = str(item)
                else:
                    val = '.'
                result += val.center(5, ' ')

            result += '\n'

        if len(self.elevator.components) > 0:
            result += 'E['
            val = ''
            for item in sorted(self.elevator.components):
                val += str(item) + ' '
            result += val.strip() + ']\n'
        return result

    def get_all_moves(self):
        loaded = self.load_elevator()

        moved = []
        for position in loaded:
            moved += position.move_elevator()
        moved = list(set(moved))

        unloaded = []
        for position in moved:
            unloaded += position.unload_elevator()
        unloaded = list(set(unloaded))

        return unloaded

    def load_elevator(self):
        current_floor = self.elevator.floor

        result = []

        if len(self.elevator.components) > 0:
            result.append(self)

        if self.elevator.open_slots() == 0:
            return result

        for i in range(0, len(self.floors[current_floor])):
            candidate = copy.deepcopy(self)
            item = candidate.floors[current_floor][i]

            candidate.elevator.components.append(item)
            candidate.floors[candidate.elevator.floor].remove(item)

            if not Component.are_all_safe(candidate.elevator.components):
                continue
            if not Component.are_all_safe(candidate.floors[candidate.elevator.floor]):
                continue

            result += Position.load_elevator(candidate)

        return list(set(result))

    def move_elevator(self):
        current_floor = self.elevator.floor
        top_floor = len(self.floors) - 1

        result = []

        if current_floor < top_floor:
            candidate = copy.deepcopy(self)
            candidate.elevator.floor += 1
            result.append(candidate)

        if current_floor > 0:
            candidate = copy.deepcopy(self)
            candidate.elevator.floor -= 1
            result.append(candidate)

        return result

    def unload_elevator(self):
        current_floor = self.elevator.floor

        floor = self.floors[current_floor]

        for item in self.elevator.components:
            floor.append(item)

        self.elevator.components.clear()

        if Component.are_all_safe(floor):
            return [self]
        else:
            return []

def parse_elements():
    with open('elements.csv', 'r') as f:
        for l in f.readlines():
            seg = l.split(',')
            ELEMENTS[seg[0].strip().upper()] = seg[1].strip()


def parse_setup(setup):
    ignored = ['a', 'an', 'and']
    position = Position()

    for i in range(0, len(setup)):
        seg = setup[i].strip().split(' ')[4:]
        floor = []
        j = 0
        while j < len(seg):
            item = seg[j].replace('-compatible', '')
            if item in ignored:
                j += 1
                continue
            if item == 'nothing':
                break

            element = item
            type_name = ''.join(ch for ch in seg[j+1] if ch not in string.punctuation)
            if type_name == 'microchip':
                floor.append(Microchip(element))
            elif type_name == 'generator':
                floor.append(Generator(element))
            else:
                raise ValueError

            j += 2
        position.floors[i] = floor
    return position

def get_goal(start: Position):
    result = Position()
    result.floors = {x: [] for x in start.floors}

    top_floor = len(result.floors) - 1

    for k in start.floors:
        result.floors[top_floor] += start.floors[k]

    result.elevator.floor = top_floor

    return result

def merge_dicts(*dict_args):
    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

def map_next_moves(node, positions):
    """
    Given a starting node return a tuple containing:
        * a graph of all possible next moves
        * a dictionary containing new positions
    """
    start_checksum = node[0]
    start = positions[start_checksum]
    candidates = start.get_all_moves()

    graph = {}
    new_positions = {}

    for candidate in candidates:
        checksum = hash(candidate)
        if checksum in positions:
            #print('Found {} again. Skipping'.format(checksum))
            # No repeats
            continue

        new_positions[checksum] = candidate
        path = node[1].copy()
        path.append(start_checksum)
        graph[checksum] = path
    return (graph, new_positions)


def process_next_level(graph, positions):
    nodes = {}
    new_positions = positions.copy()

    # for node in graph.items():
    #     result = map_next_moves(node, positions)

    #     nodes.update(result[0])
    #     new_positions.update(result[1])

    with Pool(4) as pool:
        results = pool.starmap(map_next_moves, zip(graph.items(), repeat(positions)))

    for result in results:
        nodes.update(result[0])
        new_positions.update(result[1])

    new_positions = remove_unused_positions(nodes, new_positions)
    return (nodes, new_positions)


def remove_unused_positions(graph: dict, positions: dict):
    paths = chain(*graph.values())
    keys = graph.keys()
    used = list(set(list(paths) + list(keys)))

    clean = {k:positions[k] for k in used}

    diff = len(positions) - len(clean)
    # print('{} unused positions removed'.format(diff))

    return clean


def print_sequence(items):
    print('')
    for i in range(0, len(items)):
        key = hash(items[i])
        print('Move {} - {}\n{}'.format(i, key, items[i]))


def print_node_sequence(graph, positions, key):
    if key not in graph:
        print('key {} is not in the graph'.format(key))

    path = copy.copy(graph[key])
    path.append(key)

    items = []
    for i in range(0, len(path)):
        item = path[i]
        items.append(positions[item])

    print_sequence(items)


def main():
    parse_elements()

    file_name = 'sample.txt'
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        print('Will use {} from command-line'.format(file_name))
    else:
        print('Will use default file of {}'.format(file_name))

    with open(file_name, 'r') as input_file:
        setup = input_file.readlines()

    start = parse_setup(setup)
    checksum = hash(start)
    goal = get_goal(start)
    goal_checksum = hash(goal)

    positions = {checksum: start}
    graph = {checksum: []}
    level = 0

    while goal_checksum not in positions and level < 100:
        print('{}: {} paths {} positions'.format(
            str(level).rjust(2, ' '),
            str(len(graph)).rjust(6, ' '),
            str(len(positions)).rjust(6, ' ')))

        result = process_next_level(graph, positions)

        graph = result[0]
        positions = result[1]

        level += 1

    print_node_sequence(graph, positions, goal_checksum)

if __name__ == '__main__':
    main()

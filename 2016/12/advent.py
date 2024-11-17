#! /usr/bin/env python

import sys

def main():
    file_name = 'input.txt'
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        print('Will use {} from command-line'.format(file_name))
    else:
        print('Will use default file of {}'.format(file_name))

    with open(file_name, 'r') as input_file:
        instructions = input_file.readlines()

    registers = { 
        'a': 0,
        'b': 0,
        'c': 1,
        'd': 0
    }

    i = 0
    while i < len(instructions):
        current = instructions[i].strip().split(' ')
        # print(current)
        instruction = current[0]
        increment = 1
        if instruction == 'cpy':
            if current[1] in registers.keys():
                registers[current[2]] = registers[current[1]]
            else:
                registers[current[2]] = int(current[1])
        elif instruction == 'inc':
            registers[current[1]] += 1
        elif instruction == 'dec':
            registers[current[1]] -= 1
        elif instruction == 'jnz':
            if current[1] in registers.keys():
                x = registers[current[1]]
            else:
                x = current[1]
            if x != 0:
                increment = int(current[2])
        i += increment

    print(registers)

if __name__ == '__main__':
    main()

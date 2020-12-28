from collections import deque
import re
import operator


def parse(expression, precedence):
    output = []
    stack = []
    tokens = re.split(r"([\d\+\*\(\)])\s*", expression)
    for token in (t for t in tokens if t != ""):
        if token.isdigit():
            output.append(int(token))
        elif token in precedence:
            p = precedence[token]
            while stack and stack[-1] in precedence and precedence[stack[-1]] >= p:
                output.append(stack.pop())
            stack.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while stack[-1] != "(":
                output.append(stack.pop())
            if stack[-1] == "(":
                stack.pop()  # discard
    while stack:
        output.append(stack.pop())

    return output


def calc(rpn):
    operators = {"+": operator.add, "*": operator.mul}
    result = deque(rpn)
    tmp = []
    while True:
        if len(result) == 1 and isinstance(result[0], int):
            return result.pop()
        token = result.popleft()
        if token in operators:
            result.appendleft(operators[token](tmp.pop(), tmp.pop()))
        else:
            tmp.append(token)


def main():
    input = ["1 + 2 * 3 + 4 * 5 + 6", "1 + (2 * 3) + (4 * (5 + 6))"]
    input = [row.strip() for row in open("18.txt").readlines()]

    rpn = [parse(i, {"+": 1, "*": 1}) for i in input]
    res = [calc(r) for r in rpn]
    print(f"Part 1: {sum(res)}")

    rpn = [parse(i, {"+": 2, "*": 1}) for i in input]
    res = [calc(r) for r in rpn]
    print(f"Part 2: {sum(res)}")


if __name__ == "__main__":
    main()
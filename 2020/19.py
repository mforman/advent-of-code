def parse_rules(input):
    def parse_val(v):
        if v.startswith('"'):
            return v.replace('"', "")
        else:
            return [[int(i) for i in j.split(" ")] for j in v.split(" | ")]

    return {int(pos): parse_val(val) for pos, val in (i.split(": ") for i in input)}


def match(rules, msg, stack):
    if len(stack) > len(msg):
        return False
    elif len(stack) == 0 or len(msg) == 0:
        return len(stack) == len(msg) == 0

    c = stack.pop(0)
    if isinstance(c, str):
        if msg[0] == c:
            return match(rules, msg[1:], stack.copy())
    else:
        for rule in rules[c]:
            if not isinstance(rule, list):
                rule = [rule]
            if match(rules, msg, list(rule + stack)):
                return True
    return False


def main():
    input = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
"""
    input = open("19.txt").read()

    rules, messages = (i.strip().split("\n") for i in input.split("\n\n"))
    rules = parse_rules(rules)

    matches = (match(rules, msg, list(rules[0][0])) for msg in messages)
    print(f"Part 1: {list(matches).count(True)}")

    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    matches = (match(rules, msg, list(rules[0][0])) for msg in messages)
    print(f"Part 2: {list(matches).count(True)}")


if __name__ == "__main__":
    main()

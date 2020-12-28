from collections import defaultdict

input = [
    "abc",
    "",
    "a",
    "b",
    "c",
    "",
    "ab",
    "ac",
    "",
    "a",
    "a",
    "a",
    "a",
    "",
    "b",
]

input = [row.strip() for row in open("06.txt").readlines()]

any_answer = []
all_answer = []
answers = defaultdict(int)
member_count = 0

for line in input:
    if line == "":
        any_answer.append(len(answers))
        all_answer.append(len([k for k, v in answers.items() if v == member_count]))
        answers = defaultdict(int)
        member_count = 0
        continue
    for char in line:
        answers[char] = answers[char] + 1
    member_count += 1
any_answer.append(len(answers))
all_answer.append(len([k for k, v in answers.items() if v == member_count]))

print(f"Part 1: {sum(any_answer)}")
print(f"Part 2: {sum(all_answer)}")

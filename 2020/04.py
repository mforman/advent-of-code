import re

# invalid
# input = [
#     "eyr:1972 cid:100",
#     "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
#     "",
#     "iyr:2019",
#     "hcl:#602927 eyr:1967 hgt:170cm",
#     "ecl:grn pid:012533040 byr:1946",
#     "",
#     "hcl:dab227 iyr:2012",
#     "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
#     "",
#     "hgt:59cm ecl:zzz",
#     "eyr:2038 hcl:74454a iyr:2023",
#     "pid:3556412378 byr:2007",
# ]

# valid
# input = [
#     "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
#     "hcl:#623a2f",
#     "",
#     "eyr:2029 ecl:blu cid:129 byr:1989",
#     "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
#     "",
#     "hcl:#888785",
#     "hgt:164cm byr:2001 iyr:2015 cid:88",
#     "pid:545766238 ecl:hzl",
#     "eyr:2022",
#     "",
#     "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719",
# ]

input = [row.strip() for row in open("04.txt").readlines()]

KEYS = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
EYE_COLOR = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])


def validate(d):
    try:
        if not 1920 <= int(d["byr"]) <= 2002:
            return 0

        if not 2010 <= int(d["iyr"]) <= 2020:
            return 0

        if not 2020 <= int(d["eyr"]) <= 2030:
            return 0

        hgt = d["hgt"]
        if not hgt[-2:] in ["cm", "in"]:
            return 0

        if hgt[-2:] == "cm" and not 150 <= int(hgt[:-2]) <= 193:
            return 0

        if hgt[-2:] == "in" and not 59 <= int(hgt[:-2]) <= 76:
            return 0

        if not re.match(r"^#[0-9a-fA-F]{6}$", d["hcl"]):
            return 0

        if not d["ecl"] in EYE_COLOR:
            return 0

        if not re.match(r"^[0-9]{9}$", d["pid"]):
            return 0

        return 1
    except:
        return 0


items = {}
count = 0
validated = []
for line in input:
    if line == "":
        if all(k in items for k in KEYS):
            count += 1
            if validate(items) == 1:
                validated.append(items["pid"])
            # validated += validate(items)
        items = {}
        continue
    pairs = [x.split(":") for x in line.split()]
    items = {**items, **{k: v for k, v in pairs}}
    # items = items | {k: v for k, v in pairs}

if all(k in items for k in KEYS):
    count += 1
    if validate(items) == 1:
        validated.append(items["pid"])
    # validated += validate(items)

print(f"Part 1: {count}")
print(f"Part 2: {len(validated)}")

lines = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""

orbits = {
    orbiter: target for (target, orbiter) in [x.split(")") for x in lines.splitlines()]
}


def get_orbits(orbiter, to):
    while orbiter != to:
        orbiter = orbits[orbits]
        yield orbits


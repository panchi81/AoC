def main():

    with open("day12_input.txt", "r") as fin:
        # nav = fin.read().split()
        dir = {k[0]: int(k[1:]) for k in fin.read().split()}

    E = "E"
    part_one(dir, E)

def N():
    pass


def S():
    pass


def E():
    pass


def W():
    pass


def L():
    pass


def R():
    pass


def F():
    pass


def part_one(dir, def):
    action = {"N": N, "S": S, "E": E, "W": W, "L": L, "R": R, "F": F}
    for line in dir:
        action(dir)


if __name__ == "__main__":
    main()

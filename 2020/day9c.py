# https://www.reddit.com/r/adventofcode/comments/k9vgr8/2020_day_9_part_1_python_program_giving_index_out/

from pathlib import Path


def main():

    # create puzzle data path object
    inpath = Path(
        r"C:\Users\Panchi\Documents\Pyscripts\AdventofCode2020\day9_input.txt"
    )

    # read path object contaning puzzle input
    with inpath.open(mode="r") as fin:
        data = fin.read().splitlines()

    # convert to integers
    set = [int(i) for i in data]

    # prepare the stuffs
    x = 0
    y = 25
    sums = []

    # call function dealing with the first part of the puzzle
    print(part_one(set, x, y, sums))


def part_one(set, x, y, blab):
    for i in range(x, y):
        for j in range(x + 1, y):
            blab.append(set[i] + set[j])
    if set[i + 1] not in blab:
        return set[i + 1]
    else:
        x += 1
        y += 1
        blab.clear()
        return part_one(set, x, y, blab)


if __name__ == "__main__":
    main()

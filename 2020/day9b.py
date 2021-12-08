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

    # debug
    # for c in range(len(set)):
    #     print(f"set[{c}] : {set[c]}")

    # call function dealing with the first part of the puzzle
    print(part_one(set))


def part_one(set):
    for i in range(len(set) - 26):
        subset = set[i : i + 25]
        sum = set[i + 25]
        # print(subset, sum)

        singles = []
        while subset:
            num = subset.pop()
            diff = sum - num
            if diff not in subset:
                singles.append(sum)

        singles.reverse()

    # return singles

    # for j in subset:
    #     diff = sum - j
    #     if diff in subset:  # or if diff == j
    #         return sum, diff, j


if __name__ == "__main__":
    main()

    # res = []
    # while subset:
    #     num = subset.pop()
    #     diff = sum - num
    #     if diff in subset:
    #         res.append((diff, num))
    # res.reverse()
    # return res

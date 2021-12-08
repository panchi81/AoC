from pathlib import Path

inpath = Path(r"C:\Users\Panchi\Documents\Pyscripts\AdventofCode2020\day9_input.txt")

with inpath.open(mode="r") as fin:
    puzzle = fin.read().splitlines()



def part_one(coll):
    preamble = coll[:24]
    subset = ([[False for in range(sum + 1)] for i in range(n + 1)])

    for i in range(len(coll)):
        preamble = coll[i:i+25]
        amble = coll[i+25:]
        for x in preamble:
            if int(amble[i]) == True:
                print("happy face")


part_one(puzzle)

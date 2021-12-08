from pathlib import Path

ipath = Path(r"C:\Users\Panchi\Documents\Pyscripts\AdventofCode2020\day8_input.txt")

with ipath.open(mode="r") as fin:
    inst = fin.read().splitlines()


def part_one(input):
    # return [x for x in input]                 # item for item in input
    # return [x.split() for x in input]         # command, value for item in input
    # return [x for x in enumerate(input, 1)]   # position, command value for item in input
    # return {num: com.split() for num, com in enumerate(input, 1)}
    acc = 0
    idx = {pos: 0 for pos, 0 in enumerate(input, 1)}

    for x in input:
        while idx[i] < 2:
            idx[i] += 1
            if x.split()[0] == "acc":
                acc += int(x.split()[1])
            elif x.split()[0] == "jmp":
    
                return x.split()


print(part_one(inst))

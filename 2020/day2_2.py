from pathlib import Path


def main():
    input_file = Path(
        r"C:\Users\Panchi\Documents\Pyscripts\AdventofCode2020\day2_input.txt"
    )
    with input_file.open(mode="r") as f:
        text = f.read().splitlines()
        f.close()

    arr = splitter(text)
    # print(arr)
    print(pwdefiner(arr))


def splitter(raw_text):
    ruleset = []
    for item in raw_text:
        ruleset.append(item.replace("-", " ").replace(":", " ").split())
    return ruleset


def pwdefiner(array):
    counter = 0
    for item in array:
        valid = int(item[0]) - 1
        invalid = int(item[1]) - 1
        char = item[2]
        pw = item[3]

        if pw[valid] == char and pw[invalid] != char:
            counter += 1

        # Debug
        print(valid, invalid, char, pw, pw[valid], pw[invalid], counter)
    return counter


if __name__ == "__main__":
    main()

# 371 is too low
from pathlib import Path


def main():
    input_file = Path(
        r"C:\Users\Panchi\Documents\Pyscripts\AdventofCode2020\day2_input.txt"
    )
    with input_file.open(mode="r") as f:
        text = f.read().splitlines()
        f.close()

    arr = listsplitter(text)
    # print(arr)
    print(pwdefiner(arr))


def listsplitter(raw_text):
    ruleset = []
    for item in raw_text:
        ruleset.append(item.replace("-", " ").replace(":", " ").split())
    return ruleset


def pwdefiner(array):
    counter = 0
    for item in array:
        min = int(item[0])
        max = int(item[1])
        char = item[2]
        pw = item[3]

        char_count = 0
        for i in pw:
            if i == char:
                char_count += 1

        if min <= char_count <= max:
            counter += 1

        # Debug
        # print(min, max, char, pw, char_count, counter)

    return counter


if __name__ == "__main__":
    main()

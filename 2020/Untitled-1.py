with open("day11_input.txt", "r") as fin:
    seats = [[i] for c in fin.read().split() for i in c]
    # seats = []
    # for c in fin.read().split():
    #     row = []
    #     for i in c:
    #         row.append(i)
    #     seats.append(row)


print(seats)

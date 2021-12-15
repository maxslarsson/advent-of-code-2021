from copy import deepcopy

# INFILE = 'sample.txt'
INFILE = 'input.txt'


def fold(grid, instructions):
    for ins in instructions:
        ins = ins.split(" ")[2]
        direction, amount = ins.split("=")
        amount = int(amount)
        new_grid = set()
        if direction == "x":
            for point in grid:
                if point[0] < amount:
                    new_grid.add(point)
                if point[0] > amount:
                    new_point = (amount - (point[0] - amount), point[1])
                    new_grid.add(new_point)
        elif direction == "y":
            for point in grid:
                if point[1] < amount:
                    new_grid.add(point)
                if point[1] > amount:
                    new_point = (point[0], amount - (point[1]-amount))
                    new_grid.add(new_point)
        else:
            raise ValueError(f"Unknown direction {direction} and amount {amount}")
        grid = new_grid

    return grid


def main():
    grid = set()
    with open(INFILE) as f:
        s = f.read().split("\n")
        i = 0
        while s[i] != "":
            x, y = s[i].split(",")
            grid.add((int(x), int(y)))
            i += 1

        instructions = s[i+1:]

    part1_grid = fold(deepcopy(grid), [instructions[0]])
    print(f"Part 1: {len(part1_grid)}")


if __name__ == '__main__':
    main()

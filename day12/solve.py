# INFILE = 'sample1.txt'
# INFILE = 'sample2.txt'
# INFILE = 'sample3.txt'
INFILE = 'input.txt'

NUM_PATHS_PART_1 = 0
NUM_PATHS_PART_2 = 0


def part1(graph, starting_node="start", visited=None):
    global NUM_PATHS_PART_1
    if visited is None:
        visited = []

    visited.append(starting_node)

    to_visit = graph[starting_node]
    for v in to_visit:
        if v == "end":
            NUM_PATHS_PART_1 += 1
        elif v.isupper():
            part1(graph, v, visited)
        elif v.islower():
            times_visited = visited.count(v)
            if times_visited == 0:
                part1(graph, v, visited)

    visited.pop()

    return NUM_PATHS_PART_1


def part2(graph, starting_node="start", visited=None):
    global NUM_PATHS_PART_2
    if visited is None:
        visited = []

    visited.append(starting_node)

    to_visit = graph[starting_node]
    for v in to_visit:
        if v == "end":
            NUM_PATHS_PART_2 += 1
        elif v.isupper():
            part2(graph, v, visited)
        elif v.islower():
            times_visited = visited.count(v)
            if times_visited == 0:
                part2(graph, v, visited)
            elif times_visited == 1 and v != "start":
                small_caves = list(filter(lambda x: x.islower(), visited))
                counts = map(lambda x: small_caves.count(x), small_caves)
                if 2 not in counts:
                    part2(graph, v, visited)

    visited.pop()

    return NUM_PATHS_PART_2


def main():
    with open(INFILE) as f:
        graph = {}
        for line in f.read().split("\n"):
            a, b = line.split("-")
            try:
                graph[a].append(b)
            except KeyError:
                graph[a] = [b]
            try:
                graph[b].append(a)
            except KeyError:
                graph[b] = [a]

    print(f"Part 1: {part1(graph)}")
    print(f"Part 2: {part2(graph)}")


if __name__ == '__main__':
    main()

# INFILE = 'sample1.txt'
# INFILE = 'sample2.txt'
# INFILE = 'sample3.txt'
INFILE = 'input.txt'

NUM_PATHS_PART_1 = 0


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


if __name__ == '__main__':
    main()

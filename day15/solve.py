import itertools
import math
from heapq import heappop, heappush

# INFILE = 'sample.txt'
INFILE = 'input.txt'

DX = [1, 0, -1, 0]
DY = [0, 1, 0, -1]
NUMS = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 1}


class PriorityQueue:
    pq = []  # list of entries arranged in a heap
    entry_finder = {}  # mapping of tasks to entries
    REMOVED = '<removed-task>'  # placeholder for a removed task
    counter = itertools.count()  # unique sequence count

    def empty(self):
        if len(self.pq) == 0:
            return True

        if all(task is self.REMOVED for task in self.pq):
            return True

        return False

    def add_task(self, task, priority):
        """Add a new task or update the priority of an existing task"""
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def remove_task(self, task):
        """Mark an existing task as REMOVED.  Raise KeyError if not found."""
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def get_task_priority(self, task):
        return self.entry_finder[task][0]

    def pop_task_and_priority(self):
        """Remove and return the lowest priority task. Raise KeyError if empty."""
        while self.pq:
            priority, count, task = heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task, priority
        raise KeyError('pop from an empty priority queue')


def dijkstra(grid):
    queue = PriorityQueue()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            queue.add_task((i, j), math.inf)

    # (risk, (x, y))
    queue.add_task((0, 0), 0)

    visited = set()

    vertex_mapping = {}

    while not queue.empty():
        cur, risk = queue.pop_task_and_priority()

        if cur == (len(grid) - 1, len(grid[0]) - 1):
            break

        for dx, dy in zip(DX, DY):
            next_x = cur[0] + dx
            next_y = cur[1] + dy

            if not (0 <= next_x < len(grid) and 0 <= next_y < len(grid[0])):
                continue

            if (next_x, next_y) in visited:
                continue

            next_risk = risk + grid[next_x][next_y]
            if next_risk < queue.get_task_priority((next_x, next_y)):
                vertex_mapping[(next_x, next_y)] = cur
                queue.add_task((next_x, next_y), next_risk)

        visited.add(cur)


    pos = (len(grid) - 1, len(grid[0]) - 1)
    path = []
    while pos != (0, 0):
        path.append(pos)
        pos = vertex_mapping[pos]
    path.append((0, 0))
    path.reverse()

    return path, risk


def main():
    with open(INFILE) as f:
        grid = [[int(x) for x in line] for line in f.read().split("\n")]

    best_path, lowest_risk = dijkstra(grid)
    print(f"Part 1: {lowest_risk}")



if __name__ == '__main__':
    main()

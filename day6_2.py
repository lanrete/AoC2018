from collections import Counter
import numpy as np

SIZE = 365
MAX_DISTANCE = 10000


def get_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_closest(i, j, candidate_list):
    closest = 0
    min_distance = 1000
    shared = False
    for ind, candidate in candidate_list.items():
        distance = get_distance((i, j), candidate)
        if distance == min_distance:
            shared = True
        if distance < min_distance:
            min_distance = distance
            closest = ind
            shared = False

    if not shared:
        return closest
    return -1


def get_largest(grid):
    counter = Counter(grid.ravel())
    max_area = 0
    for k, v in counter.items():
        if k in grid[:, 0]:
            continue
        if k in grid[:, -1]:
            continue
        if k in grid[0, :]:
            continue
        if k in grid[-1, :]:
            continue
        if v > max_area:
            max_area = v
    print(max_area)


def check_distance(i, j, candidate_list):
    sum_distance = 0
    for ind, candidate in candidate_list.items():
        distance = get_distance((i, j), candidate)
        sum_distance += distance
        if sum_distance >= MAX_DISTANCE:
            return False
    return True


def main():
    point = {}
    with open('input/day6.txt', 'r') as f:
        for ind, line in enumerate(f):
            x, y = [int(_) for _ in line.strip().split(',')]
            point[ind] = (x, y)
    grid = np.ndarray(shape=(SIZE, SIZE), dtype='int')
    safe_spot = 0
    for i in np.arange(0, SIZE):
        for j in np.arange(0, SIZE):
            safe_spot += check_distance(i, j, point)
    print(safe_spot)


if __name__ == '__main__':
    main()

from collections import Counter
import numpy as np

SIZE = 365


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
    """

    Parameters
    ----------
    grid: np.ndarray

    Returns
    -------

    """
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


def main():
    point = {}
    with open('input/day6.txt', 'r') as f:
        for ind, line in enumerate(f):
            x, y = [int(_) for _ in line.strip().split(',')]
            point[ind] = (x, y)
    grid = np.ndarray(shape=(SIZE, SIZE), dtype='int')
    for i in np.arange(0, SIZE):
        for j in np.arange(0, SIZE):
            belong = get_closest(i, j, point)
            grid[i, j] = belong
    print(grid)
    get_largest(grid)


if __name__ == '__main__':
    main()

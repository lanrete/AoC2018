import os
import numpy as np

def generate_area(box_string):
    box_string = box_string.split('@')[-1].strip()
    x1 = int(box_string.split(',')[0]) + 1
    y1 = int(box_string.split(':')[0].split(',')[-1]) + 1
    width, height = box_string.split(' ')[-1].split('x')
    x2 = x1 + int(width) - 1
    y2 = y1 + int(height) - 1
    return x1, x2, y1, y2


if __name__ == '__main__':
    graph = np.ndarray(shape=(1000, 1000), dtype=int)
    graph[:, :] = 0
    with open('input/day3.txt', 'r') as f:
        for line in f:
            x1, x2, y1, y2 = generate_area(line)
            graph[x1:x2+1, y1:y2+1] += 1
    print(graph)
    print('Result ==> %s' % (graph > 1).sum())

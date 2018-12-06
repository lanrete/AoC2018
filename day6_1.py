import os
import numpy as np

if __name__ == '__main__':
    x_max = 0
    y_max = 0
    with open('input/day6.txt', 'r')  as f:
        for line in f:
            x, y = [int(_) for _ in line.strip().split(',')]
            if x > x_max:
                x_max = x
            if y > y_max:
                y_max = y
    print('X max ==> %s' % x_max)
    print('Y max ==> %s' % y_max)

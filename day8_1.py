#!/usr/bin/env python
# Created by lanrete at 12/8/18


DEBUG = False
if DEBUG:
    suffix = '_sample'
else:
    suffix = ''


def process_data(s):
    raise NotImplementedError


def main():
    with open(f'input/day8{suffix}.txt', 'r') as f:
        for line in f:
            process_data(line)


if __name__ == '__main__':
    main()

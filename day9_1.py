#!/usr/bin/env python
# Created by lanrete at 12/8/18

DEBUG = False
if DEBUG:
    suffix = '_sample'
else:
    suffix = ''


def get_clockwise(marble_list, c, n):
    length = len(marble_list)
    for i in range(n):
        if c + 1 == length:
            c = 0
        else:
            c += 1
    return c


def get_counter_clockwise(marble_list, c, n):
    length = len(marble_list)
    for i in range(n):
        if c == 0:
            c = length - 1
        else:
            c -= 1
    return c


def add_to_list(marble_list, n, v):
    if n + 1 == len(marble_list):
        marble_list.append(v)
    else:
        marble_list.insert(n + 1, v)
    return marble_list


def calculate_score(player, marble):
    ans = 0
    marble_list = [0]
    current_marble = 0
    score_dict = {_: 0 for _ in range(player)}
    for i in range(1, marble + 1):
        current_player = i % player
        if i % 23 == 0:
            score_dict[current_player] += i
            loc = get_counter_clockwise(marble_list, current_marble, 7)
            score_dict[current_player] += marble_list.pop(loc)
            current_marble = loc
        else:
            loc = get_clockwise(marble_list, current_marble, 1)
            add_to_list(marble_list, loc, i)
            current_marble = loc + 1
        # print(f'[{current_player}]: {marble_list} -- [{current_marble}]')
    for k, v in score_dict.items():
        if v >= ans:
            ans = v
    print(f'Highest score is {ans}')
    return


def process_data(s):
    s = s.strip().split(' ')
    return int(s[0]), int(s[-2])


def main():
    with open(f'input/day9{suffix}.txt', 'r') as f:
        for line in f:
            player, marble = process_data(line)
            calculate_score(player, marble)


if __name__ == '__main__':
    main()

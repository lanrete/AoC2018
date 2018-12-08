#!/usr/bin/env python
# Created by lanrete at 12/8/18


DEBUG = False
if DEBUG:
    suffix = '_sample'
else:
    suffix = ''


def process_tree(ind, number_list):
    ans = 0
    sub_tree = number_list[ind]
    meta_number = number_list[ind + 1]
    ind += 2
    for i in range(sub_tree):
        sub_tree_ans, new_ind = process_tree(ind, number_list)
        ans += sub_tree_ans
        ind = new_ind
    ans += sum(number_list[ind:ind + meta_number])
    return ans, ind + meta_number


def process_data(s):
    number_list = [int(_) for _ in s.split(' ')]

    ans, ind = process_tree(0, number_list)
    print(f'Answer is ==> {ans}')

    return ans


def main():
    with open(f'input/day8{suffix}.txt', 'r') as f:
        for line in f:
            process_data(line)


if __name__ == '__main__':
    main()

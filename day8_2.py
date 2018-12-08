#!/usr/bin/env python
# Created by lanrete at 12/8/18


DEBUG = False
if DEBUG:
    suffix = '_sample'
else:
    suffix = ''


def get_value(ind, number_list):
    ans = 0
    if number_list[ind] == 0:
        meta_number = number_list[ind + 1]
        return sum(number_list[ind + 2:ind + 2 + meta_number]), ind + 2 + meta_number
    else:
        sub_tree = number_list[ind]
        meta_number = number_list[ind + 1]
        ind += 2
        sub_tree_value = []
        for i in range(sub_tree):
            sub_tree_ans, new_ind = get_value(ind, number_list)
            sub_tree_value.append(sub_tree_ans)
            ind = new_ind
        for i in range(ind, ind+meta_number):
            index = number_list[i]
            if index <= sub_tree:
                ans += sub_tree_value[index - 1]
        return ans, ind + meta_number


def process_data(s):
    number_list = [int(_) for _ in s.split(' ')]

    ans, ind = get_value(0, number_list)
    print(f'Answer is ==> {ans}')

    return ans


def main():
    with open(f'input/day8{suffix}.txt', 'r') as f:
        for line in f:
            process_data(line)


if __name__ == '__main__':
    main()

#!/usr/bin/env python
# Created by lanrete at 12/8/18

DEBUG = False
if DEBUG:
    suffix = '_sample'
else:
    suffix = ''


class Node(object):
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node
        self.previous_node = None


class NodeList(object):
    def __init__(self, head):
        self.head = head
        self.current = head
        self.head.next_node = head
        self.head.previous_node = head

    def append_after_current(self, node):
        new_node = Node(node)
        self.current.next_node.previous_node = new_node
        new_node.next_node = self.current.next_node

        self.current.next_node = new_node
        new_node.previous_node = self.current

    def delete_at_current(self):
        rv = self.current.value
        self.current.previous_node.next_node = self.current.next_node
        self.current.next_node.previous_node = self.current.previous_node
        self.current = self.current.next_node
        return rv

    def move_clockwise(self, n):
        for _ in range(n):
            self.current = self.current.next_node

    def move_counter_clockwise(self, n):
        for _ in range(n):
            self.current = self.current.previous_node


def calculate_score(player, marble):
    ans = 0
    score_dict = {_: 0 for _ in range(player)}
    node_list = NodeList(head=Node(0))
    for i in range(1, marble + 1):
        current_player = i % player
        if i % 23 == 0:
            score_dict[current_player] += i
            node_list.move_counter_clockwise(7)
            score = node_list.delete_at_current()
            score_dict[current_player] += score
        else:
            node_list.move_clockwise(1)
            node_list.append_after_current(i)
            node_list.current = node_list.current.next_node
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
            calculate_score(player, marble * 100)


if __name__ == '__main__':
    main()

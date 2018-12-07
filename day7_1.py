#!/usr/bin/env python
# Created by lanrete at 12/8/18

FLAG = ''

FINISHED = 2
STARTED = 1
IDLE = 0


class Graph(object):
    def __init__(self):
        self.end_task = {}
        self.begin_task = {}
        self.node = []
        self.node_status = {}
        pass

    def add_node(self, node):
        if node in self.node:
            return
        self.node.append(node)
        self.node_status[node] = IDLE
        self.node.sort()
        self.begin_task[node] = []
        self.end_task[node] = []
        return

    def add_edge(self, begin, end):
        self.add_node(begin)
        self.add_node(end)
        self.end_task[begin].append(end)
        self.begin_task[end].append(begin)
        return None

    def first_free_node(self):
        for node in self.node:
            if self.node_status[node] != IDLE:
                continue
            if not self.begin_task[node]:
                return node
        return None

    def is_solved(self):
        for node in self.node:
            if self.node_status[node] != FINISHED:
                return False
        return True

    def mark_finished(self, node):
        self.node_status[node] = FINISHED
        for end_node in self.end_task[node]:
            self.begin_task[end_node].remove(node)
        return None

    def solve_dependency(self):
        ans = ''
        while not self.is_solved():
            next_node = self.first_free_node()
            ans += next_node
            self.mark_finished(next_node)
        return ans


def main():
    g = Graph()
    with open(f'input/day7{FLAG}.txt', 'r') as f:
        for line in f:
            begin = line.strip().split(' ')[1]
            end = line.strip().split(' ')[-3]
            g.add_edge(begin, end)
    ans = g.solve_dependency()
    print(ans)


if __name__ == '__main__':
    main()

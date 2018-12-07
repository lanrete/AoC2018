#!/usr/bin/env python
# Created by lanrete at 12/8/18

FLAG = ''
OFFSET = 60
NUM_WORKER = 5

FINISHED = 2
STARTED = 1
IDLE = 0


def get_task_time(task):
    return OFFSET + ord(task) - ord('A') + 1


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

    def get_working_time(self, num_workers):
        timestamp = 0
        current_task = []
        time_tracking = []
        while not self.is_solved():
            print('------------------------------')
            print(f'Current time {timestamp}')
            free_task = self.first_free_node()
            new_task_list = []
            while free_task is not None and num_workers > 0:
                new_task_list.append(free_task)
                num_workers -= 1
                self.node_status[free_task] = STARTED
                print(f'Starting {free_task} at {timestamp}')
                free_task = self.first_free_node()
            new_task_tracking = list(map(lambda _: timestamp + get_task_time(_), new_task_list))
            current_task.extend(new_task_list)
            time_tracking.extend(new_task_tracking)

            if current_task:
                min_ph = 1e10
                next_task_ind = None
                for ind, time in enumerate(time_tracking):
                    if time < min_ph:
                        min_ph = time
                        next_task_ind = ind

                timestamp = min_ph
                self.mark_finished(current_task[next_task_ind])
                print(f'{current_task[next_task_ind]} finished at {timestamp}')
                num_workers += 1
                current_task.pop(next_task_ind)
                time_tracking.pop(next_task_ind)

        return timestamp


def main():
    g = Graph()
    with open(f'input/day7{FLAG}.txt', 'r') as f:
        for line in f:
            begin = line.strip().split(' ')[1]
            end = line.strip().split(' ')[-3]
            g.add_edge(begin, end)
    ans = g.get_working_time(NUM_WORKER)
    print(ans)


if __name__ == '__main__':
    main()

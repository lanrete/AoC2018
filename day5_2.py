import os

from string import ascii_lowercase

class Stack(object):
    def __init__(self):
        self.stack = []
        self.length = 0

    def peak(self):
        return self.stack[-1]

    def pop(self):
        rv = self.stack[-1]
        self.length = self.length - 1
        self.stack = self.stack[:-1]
        return rv

    def add(self, value):
        self.stack.append(value)
        self.length += 1
        return None

def react(a, b):
    if a == b:
        return False
    if a.upper() == b:
        return True
    if b.upper() == a:
        return True
    return False

def check_string(line):
    char_stack = Stack()
    for c in line:
#       print('Processing %s' % c)
        if char_stack.length == 0:
            char_stack.add(c)
#           print('Empty stack. Add into stack')
            continue
        top = char_stack.peak()
        if react(top, c):
#           print('React with current top, remove %s and %s' % (c, top))
            _ = char_stack.pop()
            continue
#       print('Doesn\'t react with top, add %s' % c)
        char_stack.add(c)
#   print('Remaining chars ==> %s' % char_stack.length)
#   print('String ==> [%s]' % ''.join(char_stack.stack))
    return char_stack.length

if __name__ == '__main__':
    shortest = 11264
    with open('input/day5.txt', 'r') as f:
        line = f.readline().strip()
        for _ in ascii_lowercase:
            removed_line = line
            removed_line = removed_line.replace(_, '')
            removed_line = removed_line.replace(_.upper(), '')
            result_len = check_string(removed_line)
            if result_len <= shortest:
                shortest = result_len
    print('Shortest ==> %s' % shortest)


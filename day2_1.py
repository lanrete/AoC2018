from collections import Counter
import os

def check_exact_time(string, ntime):
    charCounter = Counter(string)
    for k, v in charCounter.items():
        if v == ntime:
            return True
    return False


if __name__ == '__main__':
    with open('input/day2_1.txt', 'r') as f:
        exact_2 = 0
        exact_3 = 0
        for line in f:
            exact_2 += check_exact_time(line, 2)
            exact_3 += check_exact_time(line, 3)
    print('Checksum ==> %s' % (exact_2*exact_3))

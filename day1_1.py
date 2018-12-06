import os

if __name__ == '__main__':
    result = 0
    result_set = {0: ''}
    while True:
        with open('input/day1_1.txt', 'r') as f:
            for line in f:
                if line[0] == '+':
                    number = int(line[1:])
                    result += number
                if line[0] == '-':
                    number = int(line[1:])
                    result -= number
                if result in result_set.keys():
                    print('First duplicated frequency is ==> %s' % result)
                    exit()
                result_set[result] = ''
                # print('First occurence of %s' % result)
    # print('Answer for day1_1 is ==> %s' % result)

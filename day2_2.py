import os

def read_data():
    with open('input/day2_1.txt', 'r') as f:
        for line in f:
            yield line


def check_valid(first, second):
    count = 0
    samePart = []
    for a, b in zip(first, second):
        if a != b:
            count += 1
        else:
            samePart.append(a)
        if count >= 2:
            return False
    return ''.join(samePart)


if __name__ == '__main__':
    idList = list(read_data())
    for first_line in idList:
        for second_line in idList:
            if first_line == second_line:
                continue
            result = check_valid(first_line, second_line)
            if result:
                with open('output_day2.txt', 'w') as f:
                    f.write(result)
                print('Answer is ==> %s' % result)
                exit()

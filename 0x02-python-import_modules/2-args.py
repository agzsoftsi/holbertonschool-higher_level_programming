#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    if len(argv) == 1:
        print('0 arguments.')
        exit()
    numarg = len(argv) - 1
    if len(argv) == 2:
        print('{} argument:'.format(numarg))
    else:
        print('{} arguments:'.format(numarg))

    con = 0
    for n in argv:
        con = con + 1
        if con == 1:
            continue
        print('{}: {}'.format(con - 1, n))

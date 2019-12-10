#!/usr/bin/python3
for fnum in range(10):
    for snum in range(10):
        if fnum < snum:
            print('{:d}{:d}'.format(fnum, snum), end='')
            if fnum < 8:
                print(', ', end='')
print()

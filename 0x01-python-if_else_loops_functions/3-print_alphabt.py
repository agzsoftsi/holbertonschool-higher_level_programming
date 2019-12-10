#!/usr/bin/python3
for letra in range(ord('a'), ord('z') + 1):
    if letra != ord('q') and letra != ord('e'):
        print('{:c}'.format(letra), end='')

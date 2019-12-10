#!/usr/bin/python3
def uppercase(str):
    case = 0
    for letra in str:
        if ord(letra) >= ord('a') and ord(letra) <= ord('z'):
            case = 32
        else:
            case = 0
        print('{:c}'.format(ord(letra) - case), end='')
    print()

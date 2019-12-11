#!/usr/bin/python3
for letra in reversed(range(97, 123)):
    if letra % 2 != 0:
        letra = letra - 32
    print('{}'.format(chr(letra)), end='')

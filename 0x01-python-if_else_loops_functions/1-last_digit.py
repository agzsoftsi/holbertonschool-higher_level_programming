#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if number < 0:
    ld = -ld
print('Last digit of {} is {} and is'.format(number, ld), end=' ')
if ld > 5:
    print('greater than 5')
elif ld == 0:
    print('0')
else:
    print('less than 6 and not 0')

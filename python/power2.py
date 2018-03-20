#!/usr/bin/python

import sys

def power2(i):
    products = []
    x = 1
    while (i > 0):
        if (i % 2):
            products.insert(0, x)
        x = x * 2  # Multiply by 2
        i = i >> 1 # Do a shift. Is this a bug?
    # Print the powers.
    for x in products:
        print x
    return products

if __name__ == '__main__':
    value = int(sys.argv[1])
    power2(value)

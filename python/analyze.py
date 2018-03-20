#!/usr/bin/python

import sys

# Calculate the total of each increasing sequence of numbers in a
# list: 
#
#    running_total([1, 2, 1, 8, 9, 2])       == [3, 18, 2]
#    running_total([1, 3, 4, 2, 5, 4, 6, 9]) == [8, 7, 19]
#
# No checks are made for invalid inputs (e.g. strings, lists of lists
# or anything else that isn't a list of numbers.

def running_total(sequence):
    if (sequence == []):
        return []
    current = sequence[0]
    total = current
    totals = []
    for next in sequence[1:]:
        if (next <= current):
            totals.append(total)
            total = 0
        total = total + next
        current = next
    totals.append(total)
    return totals        

# Given an input file consisting of a list of numbers, one per line,
# apply running_total to the sequence and output the totals on each
# line of the output file.

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        sys.exit("Missing input file name")
    if (len(sys.argv) < 3):
        sys.exit("Missing output file name")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    source = open(input_file, 'r')
    sequence = []
    for line in source:
        sequence.append(int(line))
    source.close()

    totals = running_total(sequence)

    target = open(output_file, 'w')
    for total in totals:
        target.write(str(total))
        target.write('\n')
    target.close()

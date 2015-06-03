#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import argparse

input_file = None


def main():
    args = parse_args()
    handle_args(args)


def handle_args(args):
    input_file = open(args.input, 'r')

    for line in input_file:
        word = line.rstrip()
        Word = line.rstrip().title()
        WORD = line.rstrip().upper()

        if args.all:
            print '--all'
        if args.common:
            print '--common'
        if args.keyboard:
            print '--keyboard'
        if args.esc_numbers:
            print '--esc-numbers'
        if args.rep_numbers:
            print '--rep-numbers'
        if args.short_birth:
            print '--short-birth'
        if args.long_birth:
            print '--long-birth'
        if args.verbose:
            print '--verbose'
        if args.output:
            print '--output '+args.output
        if args.min:
            print '--min '+args.min
        if args.max:
            print '--max '+args.max


def parse_args():
    parser = argparse.ArgumentParser('rainbow.py')
    parser.add_argument('-a', '--all', help='use all options', action='store_true', default=False)
    parser.add_argument('-c', '--common', help='common combinations', action='store_true', default=False)
    parser.add_argument('-k', '--keyboard', help='keyboard combinations, word!@#€', action='store_true', default=False)
    parser.add_argument('-e', '--esc-numbers', help='escalating numbers, word1234', action='store_true', default=False)
    parser.add_argument('-r', '--rep-numbers', help='repeating numbers, word1111', action='store_true', default=False)
    parser.add_argument('-s', '--short-birth', help='short birth year, word86', action='store_true', default=False)
    parser.add_argument('-l', '--long-birth', help='long birth year, word1986', action='store_true', default=False)
    parser.add_argument('-v', '--verbose', help='run in verbose mode', action='store_true', default=False)

    required_group = parser.add_argument_group('required arguments', 'e.g: rainbow.py -i names.txt -a')
    mutex_group = required_group.add_mutually_exclusive_group(required=True)
    mutex_group.add_argument('-i', '--input',
                             dest='input',
                             metavar='<file>',
                             help='input filename')

    advanced_group = parser.add_argument_group('advanced arguments', 'e.g: rainbow.py -o rainbow.txt ')
    mutex_group = advanced_group.add_mutually_exclusive_group(required=False)
    mutex_group.add_argument('-o', '--output',
                             dest='output',
                             metavar='<file>',
                             help='output filename')
    mutex_group.add_argument('--min',
                             dest='min',
                             metavar='<number>',
                             help='min number of password characters')
    mutex_group.add_argument('--max',
                             dest='max',
                             metavar='<number>',
                             help='max number of password characters')

    test_group = parser.add_argument_group('test script', 'e.g: rainbow.py -t -a')
    mutex_group = test_group.add_mutually_exclusive_group(required=False)
    mutex_group.add_argument('-t', '--test',
                             action='store_true',
                             help='test arguments and print output in the terminal')

    args = parser.parse_args(sys.argv[1:])
    return args


# combinations
def basic(name):
    printToFile(name)
    printToFile(name.title())
    printToFile(name.upper())
    printToFile(name + name)
    printToFile(name.upper() + name.upper())
    printToFile(name + name.title())
    printToFile(name.title() + name.title())


# print name to output file
def printToFile(name):
    time.sleep(0.03)
    print name
    output_file.write(name + "\n")


# name111111111
def addNumbers(name):
    number = 0
    for i in range(0, 10):
        number = i
        res = ''
        for x in range(0, 10):
            res += str(number)
            printToFile(name + res)


# name123456789
def addRaisingNumbers(name):
    numbers = ''
    for x in range(1, 10):
        numbers = numbers + str(x)
        printToFile(name + numbers)


# name86, name1986
def addBirthYear(name, prefix):
    for x in range(1950, 2016):
        if prefix:
            printToFile(name + str(x))
        else:
            printToFile(name + str(x)[2:4])


if __name__ == "__main__":
    main()

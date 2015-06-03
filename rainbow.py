#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Implementera test
# Fixa min och max
# Catcha fel input filename fel

import sys
import argparse
import time

verbose_mode = False
run_as_test = False
output_file = open('rainbow.txt', 'w+')
# min_chars = 0
# max_chars = 12


def main():
    args = parse_args()
    handle_args(args)


def handle_args(args):

    input_file = open(args.input, 'r')
    # set_char_length(args)

    for line in input_file:
        word = line.rstrip()
        if args.all:
            print '--all'
            all_options(word)
        if args.common:
            print '--common'
            common(word)
        if args.keyboard:
            print '--keyboard'
            keyboard(word)
        if args.esc_numbers:
            print '--esc-numbers'
            escalating_numbers(word)
        if args.rep_numbers:
            print '--rep-numbers'
            repeating_numbers(word)
        if args.short_birth:
            print '--short-birth'
            birth_year(word, False)
        if args.long_birth:
            print '--long-birth'
            birth_year(word, True)
        # if args.verbose:
        #     is_verbose_mode = True


def parse_args():
    parser = argparse.ArgumentParser('rainbow.py')
    parser.add_argument('-a', '--all', help='use all options', action='store_true', default=False)
    parser.add_argument('-c', '--common', help='common combinations, wordWord', action='store_true', default=False)
    parser.add_argument('-k', '--keyboard', help='keyboard combinations, word!@#€', action='store_true', default=False)
    parser.add_argument('-e', '--esc-numbers', help='escalating numbers, word1234', action='store_true', default=False)
    parser.add_argument('-r', '--rep-numbers', help='repeating numbers, word1111', action='store_true', default=False)
    parser.add_argument('-s', '--short-birth', help='short birth year, word86', action='store_true', default=False)
    parser.add_argument('-l', '--long-birth', help='long birth year, word1986', action='store_true', default=False)
    # parser.add_argument('-v', '--verbose', help='run in verbose mode', action='store_true', default=False)

    # parser.add_argument('--min',
    #                     dest='min',
    #                     default=int(0),
    #                     metavar='<number>',
    #                     help='min number of password characters')
    # parser.add_argument('--max',
    #                     dest='max',
    #                     default=int(0),
    #                     metavar='<number>',
    #                     help='max number of password characters')

    required_group = parser.add_argument_group('required argument')
    mutex_group = required_group.add_mutually_exclusive_group(required=True)
    mutex_group.add_argument('-i', '--input',
                             dest='input',
                             metavar='FILE',
                             help='e.g: rainbow.py --input input_example.txt --all')
    # mutex_group.add_argument('-t', '--test',
    #                          action='store_true',
    #                          help='e.g: rainbow.py --test --all')

    args = parser.parse_args(sys.argv[1:])
    return args


# --all
def all_options(word):
    common(word)
    keyboard(word)
    repeating_numbers(word)
    escalating_numbers(word)
    birth_year(word, True)
    birth_year(word, False)


# --common
def common(word):
    print_to_file(word)
    print_to_file(word.title())
    print_to_file(word.upper())
    print_to_file(word + word)
    print_to_file(word.upper() + word.upper())
    print_to_file(word + word.title())
    print_to_file(word.title() + word.title())


def keyboard(word):
    for w in [word, word.title(), word.upper()]:
        print_to_file(w + '!')
        print_to_file(w + '!"')
        print_to_file(w + '!"#')
        print_to_file(w + '!"#€')
        print_to_file(w + '!"#€%')
        print_to_file(w + '!"#€%&')
        print_to_file(w + '!"#€%&/')
        print_to_file(w + '!"#€%&/(')
        print_to_file(w + '!"#€%&/()')
        print_to_file(w + '!"#€%&/()=')
        print_to_file(w + '!"#€%&/()=?')
        print_to_file(w + '!"#€%&/()=?')


# --rep-numbers
def repeating_numbers(word):
    for w in [word, word.title(), word.upper()]:
        for i in range(0, 10):
            number = i
            res = ''
            for x in range(0, 10):
                res += str(number)
                print_to_file(w + res)


# --esc-numbers
def escalating_numbers(word):
    for w in [word, word.title(), word.upper()]:
        numbers = ''
        for x in range(1, 10):
            numbers += str(x)
            print_to_file(w + numbers)


# --short-birth, --long-birth
def birth_year(word, is_long):
    for w in [word, word.title(), word.upper()]:
        for x in range(1950, 2016):
            if is_long:
                print_to_file(w + str(x))
            else:
                print_to_file(w + str(x)[2:4])


# print name to output file
def print_to_file(word):
    #time.sleep(0.03)
    print word
    output_file.write(word + "\n")

if __name__ == "__main__":
    main()

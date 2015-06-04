#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Rainbow is a simple tool for generating rainbow tables
# based on an input word list. It simply adding numbers and characters to the end of each word.
#
# Created by: 5un3x, 2015

import sys
import argparse
import time

output_file = open('rainbow.txt', 'w+')

run_as_test = False
run_in_verbose_mode = False

min_chars = 0
max_chars = 12

number_of_rows_in_file = 0
number_of_printed_words = 0

def main():
    handle_args(parse_args())

# set word min and max length
def set_length_filter(args):
    if args.min != 0:
        global min_chars
        min_chars = int(args.min)
    if args.max != 0:
        global max_chars
        max_chars = int(args.max)

# add options to word list generation
def handle_args(args):

    global run_in_verbose_mode
    run_in_verbose_mode = args.verbose
    input_file = []
    if args.input:
        input_file = open(args.input, 'r')
    else:
        input_file = [args.test]
        global run_as_test
        run_as_test = True

    set_length_filter(args)

    for line in input_file:
        global number_of_rows_in_file
        number_of_rows_in_file += 1
        word = line.rstrip()
        if args.all:
            all_options(word)
        if args.common:
            common(word)
        if args.keyboard:
            keyboard(word)
        if args.esc_numbers:
            escalating_numbers(word)
        if args.rep_numbers:
            repeating_numbers(word)
        if args.short_birth:
            birth_year(word, False)
        if args.long_birth:
            birth_year(word, True)

    print_statistics()

def parse_args():
    parser = argparse.ArgumentParser('rainbow.py')
    parser.add_argument('-a', '--all', help='use all options', action='store_true', default=False)
    parser.add_argument('-c', '--common', help='common combinations, wordWord', action='store_true', default=False)
    parser.add_argument('-k', '--keyboard', help='keyboard combinations, word!@#€', action='store_true', default=False)
    parser.add_argument('-e', '--esc-numbers', help='escalating numbers, word1234', action='store_true', default=False)
    parser.add_argument('-r', '--rep-numbers', help='repeating numbers, word1111', action='store_true', default=False)
    parser.add_argument('-s', '--short-birth', help='short birth year, word86', action='store_true', default=False)
    parser.add_argument('-l', '--long-birth', help='long birth year, word1986', action='store_true', default=False)
    parser.add_argument('-v', '--verbose', help='run in verbose mode', action='store_true', default=False)
    parser.add_argument('--min',
                        dest='min',
                        default=0,
                        metavar='<number>',
                        help='min number of password characters')
    parser.add_argument('--max',
                        dest='max',
                        default=0,
                        metavar='<number>',
                        help='max number of password characters')

    required_group = parser.add_argument_group('required argument')
    mutex_group = required_group.add_mutually_exclusive_group(required=True)
    mutex_group.add_argument('-i', '--input',
                             dest='input',
                             metavar='<file>',
                             help='e.g: rainbow.py -i input_example.txt -a')
    mutex_group.add_argument('-t', '--test',
                             metavar='<word>',
                             dest='test',
                             help='e.g: rainbow.py -t adam --all')

    return parser.parse_args(sys.argv[1:])


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

# --keyboard
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
    if not is_word_in_range(word):
        return

    global number_of_printed_words
    number_of_printed_words += 1

    if run_as_test:
        time.sleep(0.02)
        print word
    else:
        output_file.write(word + "\n")
        global run_in_verbose_mode
        if run_in_verbose_mode:
            print word

# validate word length
def is_word_in_range(word):
    global min_chars
    global max_chars
    return len(word) >= min_chars and len(word) <= max_chars

def print_statistics():
    global number_of_rows_in_file
    global number_of_printed_words
    print ''
    if not run_as_test:
        print '*** rainbow.txt has been created! ***'
    print ' Input list number of words:     '+str(number_of_rows_in_file)
    print ' Output list number of words:    '+str(number_of_printed_words)
    print ' Combinations per word:          '+str(number_of_printed_words / number_of_rows_in_file)
    print ''

if __name__ == "__main__":
    main()

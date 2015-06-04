##Rainbow

####Rainbow Table Generating Tool, v1.0.
Rainbow is a simple tool for generating rainbow tables based on an input word list. It simply adding numbers and characters to the end of each word. View usage below for options description.

###Example
######View /example folder for an output example

###Make script executable

	$ chmod +x rainbow.py

###Usage
######Creating a output txt file based on <input_text_file> with all options activated
    ./rainbow.py -i <input_text_file> --all
    
###Test
######Printing the result of all options activated based on the word 'richard' in the terminal
    ./rainbow.py -t richard --all
    
###Rainbow Usage

    usage: rainbow.py [-h] [-a] [-c] [-k] [-e] [-r] [-s] [-l] [--min <number>]
                  [--max <number>] (-i FILE | -t WORD)

    optional arguments:
      -h, --help            show this help message and exit
      -a, --all             use all options
      -c, --common          common combinations, wordWord
      -k, --keyboard        keyboard combinations, word!@#€
      -e, --esc-numbers     escalating numbers, word1234
      -r, --rep-numbers     repeating numbers, word1111
      -s, --short-birth     short birth year, word86
      -l, --long-birth      long birth year, word1986
      --min <number>        min number of password characters
      --max <number>        max number of password characters

    required argument:
      -i FILE, --input FILE
                            e.g: rainbow.py -i input_example.txt -a
      -t WORD, --test WORD  e.g: rainbow.py -t adam --all


###Change log
######2015-06-04 - Version 1.0
   

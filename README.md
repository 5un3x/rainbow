#Make script executable

	$ chmod +x rainbow.py


#Example (run with all options)

    ./rainbow.py -i <input_text_file> --all
    
#Rainbow Usage

    usage: rainbow.py [-h] [-a] [-c] [-k] [-e] [-r] [-s] [-l] -i FILE

    optional arguments:
      -h, --help            show this help message and exit
      -a, --all             use all options
      -c, --common          common combinations, wordWord
      -k, --keyboard        keyboard combinations, word!@#€
      -e, --esc-numbers     escalating numbers, word1234
      -r, --rep-numbers     repeating numbers, word1111
      -s, --short-birth     short birth year, word86
      -l, --long-birth      long birth year, word1986

    required argument:
      -i FILE, --input FILE
                            e.g: rainbow.py --input input_example.txt --all

#Changelog
    No changes
   

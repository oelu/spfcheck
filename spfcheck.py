#!/usr/local/bin/python2.7
"""Check SPF records

Usage:
    spfcheck.py (-i <ipaddr> -s <sender> -m <host>) [options]

Options:
    -h, --help      show help message
    -v, --verbose   print out verbose messages

"""
__author__ = 'olivier'

# import statements
from docopt import docopt
from pprint import pprint
import spf


def main():
    """
    main function

    assigns arguments from docopt and calls spf.check() function
    """
    # gets arguments from docopt
    arguments = docopt(__doc__)
    # assigns docopt arguments
    ipaddr = arguments['<ipaddr>']
    host = arguments['<host>']
    sender = arguments['<sender>']
    verbose = arguments.get('--verbose')

    if verbose:
        print "script called with: "
        print arguments

    result = spf.check(i=ipaddr, s=sender, h=host)
    pprint(result)

if __name__ == "__main__":
    main()

# spfcheck.py
Simple wrapper around pyspf. See: https://pypi.python.org/pypi/pyspf/

## Usage

```sh
$ ./spfcheck.py --help
Check SPF records

Usage:
    spfcheck.py (-i <ipaddr> -s <sender> -m <host>) [options]

Options:
    -h, --help      show help message
    -v, --verbose   print out verbose messages
```

## Example

```sh
$ ./spfcheck.py -i 74.125.142.26 -s test@gmail.com  -m alt3.gmail-smtp-in.l.google.com
('pass', 250, 'sender SPF authorized')
```

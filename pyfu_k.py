# https://github.com/NKID00/pyfu_k
# Copyright (c) 2021 NKID00
# SPDX-License-Identifier: MIT

from functools import lru_cache
from argparse import ArgumentParser

__all__ = ['pyfu_k', 'VERSION']

VERSION = 'pyfu_k v0.3.2 with pyfu_k algorithm v0.2.0'


@lru_cache()
def _pyfu_k_number(number: int) -> str:
    '''Convert an integer number to a pyfu_k string.'''
    data = {
        1: '(()==())',
        2: '(()==())+(()==())',
        3: '(()==())+(()==())+(()==())',
        4: '(()==())+(()==())+(()==())+(()==())',
        5: '(()==())+(()==())+(()==())+(()==())+(()==())',
        6: '((()==())+(()==()))*((()==())+(()==())+(()==()))',
        7: '(()==())+((()==())+(()==()))*((()==())+(()==())+(()==()))',
        8: '((()==())+(()==()))**((()==())+(()==())+(()==()))',
        9: '((()==())+(()==())+(()==()))**((()==())+(()==()))',
        10: '(()==())+((()==())+(()==())+(()==()))**((()==())+(()==()))',
    }
    if number > 10:
        if number % 10 == 0:
            return '(%s)*(%s)' % (
                '()==()' if number // 10 == 1  # get rid of the useless parens.
                else _pyfu_k_number(number // 10),
                data[10]
            )
        else:
            return '%s+(%s)*(%s)' % (
                _pyfu_k_number(number % 10),
                '()==()' if number // 10 == 1  # get rid of the useless parens.
                else _pyfu_k_number(number // 10),
                data[10]
            )
    else:
        return data[number]


def pyfu_k(expression: str, no_exec: bool = False) -> str:
    '''Convert a python expression to a pyfu_k string.'''
    data = {
        0: '()==(()==())',
        1: '()==()',
    }
    return ('%s' if no_exec else 'exec(%s)') % '+'.join(map(
        lambda c: 'chr(%s)' % (
            data[ord(c)] if c in '\x00\x01'  # get rid of the useless parens.
            else _pyfu_k_number(ord(c))
        ), expression
    ))


def main():
    parser = ArgumentParser(
        description='Convert Python codes into 10 different characters: '
                    'cehrx()=+*'
    )
    parser.add_argument('-v', '--version', action='version', version=VERSION)
    parser.add_argument(
        '--no-exec', action='store_true',
        help="remove the 'exec' function call in the converted code"
    )
    parser.add_argument(
        '--no-count', action='store_true',
        help="disable the characters counting functionality"
    )
    parser.add_argument(
        'code', nargs='?',
        help='code for the conversion (interactive mode if not given)'
    )

    args = parser.parse_args()

    if args.code is None:
        print('Use Ctrl-C to exit.')
        try:
            while True:
                result = pyfu_k(input('(pyfu_k) '), args.no_exec)
                print(result)
                if not args.no_count:
                    print('(%s characters)' % len(result))
        except KeyboardInterrupt:
            pass
    else:
        result = pyfu_k(args.code, args.no_exec)
        print(result)
        if not args.no_count:
            print('(%s characters)' % len(result))


if __name__ == '__main__':
    main()

from functools import lru_cache

__all__ = ['pyfu_k']


@lru_cache()
def _pyfu_k_number(number: int) -> str:
    '''Convert an integer number to a PyFu_k string.'''
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


def pyfu_k(expression: str) -> str:
    '''Convert a python expression to a PyFu_k string.'''
    data = {
        0: '()==(()==())',
        1: '()==()',
    }
    return 'exec(%s)' % '+'.join(map(
        lambda c: 'chr(%s)' % (
            data[ord(c)] if c in '\x00\x01'  # get rid of the useless parens.
            else _pyfu_k_number(ord(c))
        ), expression
    ))


def main():
    print('pyfu_k v0.3.1 with PyFu_k algorithm v0.2.0')
    print('https://github.com/NKID00/pyfu_k')
    print('Copyright (c) 2021 NKID00')
    print('License: MIT License')
    print('Use Ctrl-C to exit.')
    print()
    try:
        while True:
            print(pyfu_k(input('(PyFu_k) ')))
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()

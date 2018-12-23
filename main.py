#!/usr/bin/env python3

import argparse
import pyperclip
import string
import random

def random_password(length=10, options={}):
    chars = {
        'lower': string.ascii_lowercase,
        'upper': string.ascii_uppercase,
        'num': string.digits,
        'sym': string.punctuation,
    }

    if 'exclude' in options:
        for exclusion in options['exclude']:
            chars.pop(exclusion)

    allowed_chars = ''.join(list(chars.values()))
    return ''.join(random.choice(allowed_chars) for i in range(length))


def generate_password():
    parser = argparse.ArgumentParser()
    parser.add_argument('password_length', type=int, nargs='?', help='password length, default is 10')
    parser.add_argument('--no', action='append', choices=['lower', 'upper', 'num', 'sym'], help='characters to exclude')
    args = parser.parse_args()

    options = {
        'exclude': args.no,
    }
    password = random_password(args.password_length or 10, options)

    pyperclip.copy(password)
    print(password)
    return password


if __name__ == '__main__':
    generate_password()

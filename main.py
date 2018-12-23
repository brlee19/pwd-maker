#!/usr/bin/env python3

import sys, pyperclip, string, random

# take in length as an arg
# create random pwd of that length
    # TODO: expand other options (whether to include letters, numbers, symbols)
# print it
# copy it into the clipboard


def random_password(length, options=None):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def main():
    password = random_password(10)
    print(password)
    pyperclip.copy(password)
    pyperclip.paste()


main()

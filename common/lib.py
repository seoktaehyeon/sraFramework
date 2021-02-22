#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random


def hello_world():
    _first_name = (
        'will',
        'wei'
    )
    _last_name = (
        'shi',
        'stone'
    )
    _str = [
        random.choice(_first_name).capitalize(),
        random.choice(('', ' ', '-')),
        random.choice(_last_name).capitalize(),
    ]
    return ''.join(_str)


if __name__ == '__main__':
    print('This is common lib')

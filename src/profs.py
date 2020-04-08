# -*- coding: utf-8 -*-
"""Profiles for Skaffold (profs)
"""


import yaml


def profs():
    document = """
      a: 1
      b:
        c: 3
        d: 4
    """
    print(yaml.dump(yaml.load(document)))


if __name__ == '__main__':
    profs()

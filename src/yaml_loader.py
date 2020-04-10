# -*- coding: utf-8 -*-
"""
   Styler Template Environment Variable Extractor (Steve)

   Component: YAML file loader

"""


from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def load_yaml_file(path: str) -> dict:
    """ Loads a YAML file.

    Arguments:
        path: Path to the YAML file to load.

    Returns:
        A dictionary of the YAML file contents.

    """
    stream = open(path, 'r')
    return load(stream, Loader=Loader)

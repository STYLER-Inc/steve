# -*- coding: utf-8 -*-
"""
   Styler Template Environment Variable Extractor (Steve)
"""

import fire

from jinja2 import Environment, FileSystemLoader, Template
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def load_jija_template_from_filesystem(paths: list) -> FileSystemLoader:
    """ Loads a template.

    Arguments:
        paths: Paths to be searched for templates.

    Returns:
        The initialised FileSystemLoader.

    """
    return FileSystemLoader(paths)


def get_template_env(fs_loader: FileSystemLoader) -> Environment:
    """ Gets a environment for a template

    Arguments:
        fs_loader: An initialised jinja2.FileSystemLoader object.

    Returns:
        The loaded jinja2.Environment

    """
    return Environment(loader=fs_loader)


def load_yaml_file(path: str) -> dict:
    """ Loads a YAML file.

    Arguments:
        path: Path to the YAML file to load.

    Returns:
        A dictionary of the YAML file contents.

    """
    stream = open(path, 'r')
    return load(stream, Loader=Loader)


def split_file_path(full_file_path: str, dir_separator: str = '/') -> list:
    """ Splits the filepath at the last `dir_separator` to extract the
    filepath and the filename.

    Example:
        Input:  '/path/to/file.ext'
        Output: ['/path/to/', 'file.ext']

    Arguments:
        full_file_path: A full file path.
        dir_separator (optional): Directory separator.

    Returns:
        List consisting of filepath and filename.

    """
    return full_file_path.rsplit(f'{dir_separator}', 1)


def load_template(template_file: str) -> Template:
    """ Loads a single template from the given file path.

    Arguments:
        template_file: Full or relative path to template file.

    Returns:
        Template object.

    """
    split_path = split_file_path(template_file)
    template_path, template_filename = [split_path[i] for i in (0, 1)]
    fs_loader = load_jija_template_from_filesystem(template_path)
    template_env = get_template_env(fs_loader)
    return template_env.get_template(template_filename)


def render_single_template(template_file: str,
                           values_file: str) -> str:
    """ Renders a single template file with values extracted
    from a single values file.

    Arguments:
        template_file: Template file full/relative path.
        values_file: Values file full/relative path.

    Returns:
        Output of rendered template.

    """
    # Load
    values = load_yaml_file(values_file)
    template = load_template(template_file)

    # Render
    return template.render(values)


if __name__ == '__main__':
    fire.Fire(render_single_template)

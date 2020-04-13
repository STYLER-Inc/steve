# -*- coding: utf-8 -*-
"""
   Styler Template Environment Variable Extractor (Steve)

   Component: Template Loader

"""

from jinja2 import Environment, FileSystemLoader, Template


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

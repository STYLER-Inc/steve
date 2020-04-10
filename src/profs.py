# -*- coding: utf-8 -*-
"""
   Styler Template Environment Variable Extractor (Steve)
"""

import yaml

from jinja2 import Environment, FileSystemLoader, Template


def load_templates(paths: list) -> FileSystemLoader:
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
    stream = open('src/values.yaml', 'r')
    return yaml.load(stream)


def render_templates(template_dirs: list, values_file_path: str) -> str:
    """ Renders a single, or multiple templates.

    Arguments:
        template_dirs: Places in which to look for templates.
        values_file_path: YAML file to use as a source for values.

    Returns:
        Rendered template(s).
    """
    values = load_yaml_file(values_file_path)

    fs_loader = load_templates(template_dirs)
    template_env = get_template_env(fs_loader)
    template = template_env.get_template('skaffold.yaml')
    return template.render(values)


if __name__ == '__main__':
    render_results = render_templates(template_dirs=['src/'], values_file_path='src/values.yaml')
    print(render_results)

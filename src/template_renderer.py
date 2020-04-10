# -*- coding: utf-8 -*-
"""
   Styler Template Environment Variable Extractor (Steve)

   Component: Template Renderer

"""

from yaml_loader import load_yaml_file
from template_loader import load_template

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

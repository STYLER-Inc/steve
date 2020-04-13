# -*- coding: utf-8 -*-
"""
   Styler Template Environment Variable Extractor (Steve)

   Component: Main

"""

from fire import Fire

from template_renderer import render_single_template


if __name__ == '__main__':
    Fire(render_single_template)

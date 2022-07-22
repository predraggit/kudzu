# -*- coding: utf-8 -*-

"""Top-level package for kudzu."""

__author__ = "Predrag Vasiljevic"
__email__ = "predrag.v94@gmail.com"
# Do not edit this string manually, always use bumpversion
# Details in CONTRIBUTING.md
__version__ = "0.0.0"


def get_module_version():
    return __version__


from .example import Example  # noqa: F401

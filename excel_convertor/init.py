"""
Excel Convertor

A configurable tool for transferring data between Excel workbooks.
"""

__version__ = "0.1.0"

from .converter import convert

__all__ = [
    "convert",
]

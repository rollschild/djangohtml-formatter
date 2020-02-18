"""This file contains utilities to decribe a (regex) pattern"""
from typing import Pattern as RegexPattern, Match as RegexMatch, Optional

from ..core.inputscanner import InputScanner

__all__ = ["Pattern"]


class Pattern:
    """Parent class of all patterns"""

    def __init__(self, input_scanner: InputScanner, parent=None) -> None:
        self._input_scanner = input_scanner
        self._starting_pattern: Optional[RegexPattern] = None
        self._match_pattern: Optional[RegexPattern] = None

    def read(self) -> str:
        res = self._input_scanner.read(self._starting_pattern)
        #  if (self._starting_pattern is None) or res:
        return res

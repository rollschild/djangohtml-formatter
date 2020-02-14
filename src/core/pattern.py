"""This file contains utilities to decribe a (regex) pattern"""
from ..core.inputscanner import InputScanner

__all__ = ["Pattern"]


class Pattern:
    def __init__(self, input_scanner: InputScanner, parent=None) -> None:
        self._input_scanner = input_scanner

"""Main input scanner utility to read input string"""
#  import re


class InputScanner:
    """Main class for the scanner utilities"""

    def __init__(self, input_string):
        if input_string is None:
            input_string = ""

        self._input = input_string
        self._input_length = len(self._input)
        self._next_read_position = 0

    def reset(self):
        """Start over"""
        self._next_read_position = 0

    def back(self):
        """Go back one position"""
        if self._next_read_position > 0:
            self._next_read_position -= 1

    def can_read_next(self):
        """Whether we can read the next position or not"""
        return self._next_read_position < self._input_length

    def read_next(self):
        """
        Read the next position and return the value;
        Update position
        """
        val = None
        if self.can_read_next():
            val = self._input[self._next_read_position]
            self._next_read_position += 1

        return val

    def peek(self, index=0):
        """Peek {index} positions ahead and return the value"""
        val = None
        index += self._next_read_position
        if 0 <= index < self._input_length:
            val = self._input_length[index]

        return val

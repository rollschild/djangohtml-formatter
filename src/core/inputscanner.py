"""Main input scanner utility to read input string"""
#  import re


class InputScanner:
    """Main class for the scanner utilities"""

    def __init__(self, input_string: str) -> None:
        if input_string is None:
            input_string = ""

        self._input: str = input_string
        self._input_length: int = len(self._input)
        self._next_read_position: int = 0

    def reset(self) -> None:
        """Start over"""
        self._next_read_position = 0

    def back(self) -> None:
        """Go back one position"""
        if self._next_read_position > 0:
            self._next_read_position -= 1

    def can_read_next(self) -> bool:
        """Whether we can read the next position or not"""
        return self._next_read_position < self._input_length

    def read_next(self) -> str:
        """
        Read the next position and return the value;
        Update position
        """
        val: str = ""
        if self.can_read_next():
            val = self._input[self._next_read_position]
            self._next_read_position += 1

        return val

    def peek(self, index: int = 0) -> str:
        """Peek {index} positions ahead and return the value"""
        val: str = ""
        index += self._next_read_position
        if 0 <= index < self._input_length:
            val = self._input[index]

        return val

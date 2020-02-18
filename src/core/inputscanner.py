"""Main input scanner utility to read input string"""
import re
from typing import (
    Pattern as RegexPattern,
    Optional,
    Union,
    Match as RegexMatch,
)


class InputScanner:
    """
    Main class for the scanner utilities
    Read raw strings
    """

    def __init__(self, input_string: str) -> None:
        self.__six = __import__("six")
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

    def generate_regex(
        self,
        pattern: Union[str, Optional[RegexPattern[str]]],
        match_from: bool = False,
    ) -> Optional[RegexPattern]:
        result: Optional[RegexPattern] = None
        if isinstance(pattern, self.__six.string_types) and pattern != "":
            result = re.compile(pattern)
        elif (
            pattern is not None
            and bool(pattern)
            and type(pattern) == RegexPattern[str]
        ):
            #  elif pattern is not None and isinstance(pattern, RegexPattern[str]):
            # TODO: fix the mypy warning
            result = re.compile(pattern.pattern)

        return result

    def match(self, pattern: RegexPattern[str]) -> Optional[RegexMatch[str]]:
        """
        Read a portion of the input string and match with the regex pattern
        Update read position; Return the match object
        """
        pattern_match: Optional[RegexMatch[str]] = None
        if self.can_read_next():
            pattern_match = pattern.match(
                self._input, self._next_read_position
            )
            if pattern_match is not None and bool(pattern_match):
                # update next read position
                self._next_read_position = pattern_match.end(0)

        return pattern_match

    def read(self, starting_pattern: Optional[RegexPattern[str]]) -> str:
        """
        Read input string and return a result string matching the
        starting_pattern
        """
        res: str = ""
        pattern_match: Optional[RegexMatch[str]] = None
        if starting_pattern and bool(starting_pattern):
            pattern_match = self.match(starting_pattern)
            if pattern_match is not None and bool(pattern_match):
                res = pattern_match.group(0)

        return res

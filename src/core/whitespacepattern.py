import re
from typing import Optional, TypeVar, Pattern as RegexPattern
from ..core.pattern import Pattern
from ..core.inputscanner import InputScanner

__all__ = ["WhitespacePattern"]

WhitespacePatternType = TypeVar(
    "WhitespacePatternType", bound="WhitespacePattern"
)


class WhitespacePattern(Pattern):
    """Child class of Pattern"""

    def __init__(
        self,
        input_scanner: InputScanner,
        parent: Optional[WhitespacePatternType] = None,
    ) -> None:
        super(WhitespacePattern, self).__init__(input_scanner, parent)
        self.whitespace_before_token = ""  # private???
        self.newline_count = 0
        self._newline_regexp: Optional[RegexPattern[str]] = None
        if parent is not None:
            self._newline_regexp = self._input_scanner.generate_regex(
                parent._newline_regexp
            )
        else:
            self._set_whitespace_patterns("", "")

    def _set_whitespace_patterns(
        self, whitespace_chars: str, newline_chars: str
    ) -> None:
        """Define whitespace patterns"""
        whitespace_chars += "\t "
        newline_chars += "\n\r"

        # the regex pattern to match one or more whitespaces or newlines
        # NOTICE THE ONE OR MORE SYMBOL +
        self._match_pattern = self._input_scanner.generate_regex(
            "[" + whitespace_chars + newline_chars + "]+"
        )

        # the regex pattern to match newline characters
        self._newline_regexp = self._input_scanner.generate_regex(
            "\r\n|[" + newline_chars + "]"
        )

    def read(self) -> str:
        """
        Call the read() method from InputScanner to read in
        whitespaces/newlines
        """
        self.newline_count = 0
        self.whitespace_before_token = ""
        res: str = self._input_scanner.read(self._match_pattern)
        if res == " ":
            self.whitespace_before_token = " "
        elif bool(res) and self._newline_regexp is not None:
            # matched a newline!
            # res is the newline character
            # Pattern.split(str) === re.split(Pattern, str, ...)
            # determine how many new lines
            lines = self._newline_regexp.split(res)  # total
            self.newline_count = len(lines) - 1  # number of new lines
            self.whitespace_before_token = lines[-1]

        return res

"""
Tokenizer is the utility to read/parse an input string
...and generate tokens
"""

import dataclasses
import re
from typing import List, Optional, Pattern as RegexPattern

from ..core.inputscanner import InputScanner
from ..core.token import Token
from ..core.tokenstream import TokenStream
from ..core.whitespacepattern import WhitespacePattern


@dataclasses.dataclass
class TokenTypes:
    """Built-in token types"""

    START: str = "TK_START"
    RAW: str = "TK_RAW"
    EOF: str = "TK_EOF"


TOKEN_TYPES = TokenTypes()


class TokenizerPatterns:
    def __init__(self, inputscanner: InputScanner):
        self.whitespace = WhitespacePattern(inputscanner)
        # possibly other patterns to follow


class Tokenizer:
    """Tokenizer is the main class to tokenize an input string"""

    def __init__(self, input_string: str) -> None:
        self._input_scanner: InputScanner = InputScanner(input_string)
        self._tokenstream: Optional[TokenStream] = None
        self._patterns: TokenizerPatterns = TokenizerPatterns(
            self._input_scanner
        )

    def tokenize(self) -> TokenStream:
        """
        this is the main tokenize method
        read each token and add to TokenStream
        """
        self._input_scanner.reset()
        self._tokenstream = TokenStream()

        current_token: Optional[Token] = None
        previous_token: Token = Token(TokenTypes.START, "")
        open_token: Optional[Token] = None
        open_stack: List[Optional[Token]] = []
        comments = TokenStream()

        while previous_token.token_type != TOKEN_TYPES.EOF:
            # current_token is valid
            current_token = self._get_next_token_with_comments(
                previous_token, open_token
            )

            if current_token is not None:
                if self._is_open(current_token):
                    open_stack.append(current_token)
                    open_token = current_token
                elif open_token is not None and self._is_closed(
                    current_token, open_token
                ):
                    current_token.opened_peer = open_token
                    open_token.closed_peer = current_token
                    open_stack.pop()
                    if open_stack:
                        open_token = open_stack[-1]
                    else:
                        open_token = None
                    current_token.parent_token = open_token

                self._tokenstream.add(current_token)
                previous_token = current_token

        return self._tokenstream

    def _is_open(self, current_token: Token) -> bool:
        return False

    def _is_closed(self, current_token: Token, open_token: Token) -> bool:
        return False

    def _get_next_token_with_comments(
        self, previous: Token, open_token: Optional[Token]
    ) -> Token:
        current_token = self._get_next_token(previous, open_token)
        current_token.parent_token = open_token
        current_token.previous_token = previous
        return current_token

    def _get_next_token(
        self, previous_token: Token, open_token: Optional[Token]
    ) -> Token:
        # Skip spaces and newlines
        self._read_white_space()
        res: Optional[str] = self._input_scanner.read(re.compile(r".+"))
        if res:
            return self._create_token(TOKEN_TYPES.RAW, res)

        return self._create_token(TOKEN_TYPES.EOF, "")

    def _read_white_space(self) -> str:
        return self._patterns.whitespace.read()

    def _create_token(self, token_type: str, text: str) -> Token:
        token: Token = Token(
            token_type,
            text,
            self._patterns.whitespace.newline_count,
            self._patterns.whitespace.whitespace_before_token,
        )
        return token

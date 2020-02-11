"""
Tokenizer is the utility to read/parse an input string
...and generate tokens
"""

import dataclasses
from typing import List, Optional

from ..core.inputscanner import InputScanner
from ..core.token import Token
from ..core.tokenstream import TokenStream


@dataclasses.dataclass
class TokenTypes:
    """Built-in token types"""

    START: str = "START_TOKEN"
    RAW: str = "RAW_TOKEN"
    EOF: str = "EOC_TOKEN"


TOKEN_TYPES = TokenTypes()


class Tokenizer:
    """Tokenizer is the main class to tokenize an input string"""

    def __init__(self, input_string: str) -> None:
        self._input_scanner: InputScanner = InputScanner(input_string)
        self._tokens: List[Token] = []

    def tokenize(self):
        """this is the main tokenize method"""
        self._input_scanner.reset()
        self._tokens = TokenStream()

        current_token: Optional[Token] = None
        previous_token: Token = Token(TokenTypes.START, "")
        open_token: Optional[Token] = None
        open_stack: List[Token] = []
        comments = TokenStream()

        while previous_token.token_type != TOKEN_TYPES.EOF:
            # current_token is valid
            current_token = self._get_next_token_with_comments(
                previous_token, open_token
            )

        def _get_next_token_with_comments(
            self, previous: Token, open_token: Token
        ) -> Token:
            current_token = self._get_next_token(previous, open_token)
            current_token.parent_token = open_token
            current_token.previous_token = previous
            return current_token

        def _get_next_token(self, previous_token: Token, open_token: Token) -> Token:
            self._read_white_space()  # TODO
            val: Token = Token(TokenTypes.START, "")
            return val

"""
This file contains utilities regarding TokenStream,
...a list of tokens
"""
from typing import List, Optional, TypeVar

from ..core.token import Token

TokenStreamType = TypeVar("TokenStreamType", bound=TokenStream)


class TokenStream:
    """Main class"""

    def __init__(self, parent_token: Optional[Token] = None) -> None:
        self._tokens: List[Token] = []
        self._tokens_length: int = len(self._tokens)
        self._next_read_position: int = 0
        self._parent_token: Optional[Token] = parent_token

    def reset(self) -> None:
        """Start over: reset to the beginning of the tokens list"""
        self._next_read_position = 0

    def is_empty(self) -> bool:
        """Is the tokens list empty?"""
        return self._tokens_length == 0

    def can_read_next(self) -> bool:
        """Have we reached end of the tokens list?"""
        return self._next_read_position < self._tokens_length

    def read_next(self) -> Token:
        """Read next token from the tokens list"""
        if self.can_read_next():
            val = self._tokens[self._next_read_position]
            self._next_read_position += 1
            return val

        raise StopIteration

    def peek(self, index: int = 0) -> Optional[Token]:
        """Peek {index} positions ahead"""
        index += self._next_read_position
        val: Optional[Token] = None
        if 0 <= index < self._tokens_length:
            val = self._tokens[index]

        return val

    def add(self, token: Token) -> None:
        """Add a token to the tokens list"""
        self._tokens.append(token)
        self._tokens_length += 1

    def __iter__(self: TokenStreamType) -> TokenStreamType:
        self.reset()
        return self

    def __next__(self) -> Token:
        return self.read_next()

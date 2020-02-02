"""
This file contains utilities regarding TokenStream,
...a list of tokens
"""


class TokenStream:
    """Main class"""

    def __init__(self, parent_token=None):
        self._tokens = []
        self._tokens_length = len(self._tokens)
        self._next_read_position = 0
        self._parent_token = parent_token

    def reset(self):
        """Start over: reset to the beginning of the tokens list"""
        self._next_read_position = 0

    def is_empty(self):
        """Is the tokens list empty?"""
        return self._tokens_length == 0

    def can_read_next(self):
        """Have we reached end of the tokens list?"""
        return self._next_read_position < self._tokens_length

    def read_next(self):
        """Read next token from the tokens list"""
        if self.can_read_next():
            val = self._tokens[self._next_read_position]
            self._next_read_position += 1
            return val

        raise StopIteration

    def peek(self, index=0):
        """Peek {index} positions ahead"""
        index += self._next_read_position
        val = None
        if 0 <= index < self._tokens_length:
            val = self._tokens[index]

        return val

    def add(self, token):
        """Add a token to the tokens list"""
        self._tokens.append(token)
        self._tokens_length += 1

    def __iter__(self):
        self.reset()
        return self

    def __next__(self):
        return self.read_next()

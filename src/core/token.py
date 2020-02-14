"""Definition of Token"""
from typing import TypeVar, Optional, Generic

TokenType = TypeVar("TokenType", bound="Token")


class Token(Generic[TokenType]):
    """Main Token class"""

    # TODO: rename the type parameter
    def __init__(
        self,
        token_type: str,
        text: str,
        newlines: int = 0,
        leading_whitespace: str = "",
    ) -> None:
        self.token_type: str = token_type
        self.text = text
        self.newlines = newlines
        self.leading_whitespace = leading_whitespace
        self.leading_comments = None
        self.parent_token: Optional[TokenType] = None
        self.next = None
        self.previous_token: Optional[TokenType] = None
        self.opened_peer: Optional[TokenType] = None
        self.closed_peer: Optional[TokenType] = None
        self.directives = None

"""Definition of Token"""


class Token:
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
        self.parent = None
        self.next = None
        self.previous = None
        self.opened = None
        self.closed = None
        self.directives = None

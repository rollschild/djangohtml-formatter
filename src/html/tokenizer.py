import re
import dataclasses

from ..core.inputscanner import InputScanner
from ..core.tokenizer import (
    TokenTypes as BaseTokenTypes,
    Tokenizer as BaseTokenizer,
    TokenizerPatterns as BaseTokenizerPatterns,
)
from ..core.pattern import Pattern

__all__ = ["TokenTypes"]


@dataclasses.dataclass
class TokenTypes(BaseTokenTypes):
    """Token types for Django Template HTML"""

    TAG_OPEN = "TK_TAG_OPEN"
    TAG_CLOSE = "TK_TAG_CLOSE"
    TEMPLATE_OPEN = "TK_TEMPLATE_OPEN"
    TEMPLATE_CLOSE = "TK_TEMPLATE_CLOSE"
    ATTRIBUTE = "TK_ATTRIBUTE"
    EQUALS = "TK_EQUALS"
    VALUE = "TK_VALUE"
    COMMENT_OPEN = "TK_COMMENT_OPEN"
    COMMENT_CLOSE = "TK_COMMENT_CLOSE"
    TEXT = "TK_TEXT"
    UNKNOWN = "TK_UNKNOWN"
    VARIABLE_OPEN = "TK_VARIABLE_OPEN"
    VARIABLE_CLOSE = "TK_VARIABLE_CLOSE"


TOKEN_TYPES = TokenTypes()

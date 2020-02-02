"""
Tokenizer is the utility to read/parse an input string
...and generate tokens
"""

import dataclasses

from ..core.inputscanner import InputScanner
from ..core.token import Token
from ..core.tokenstream import TokenStream


@dataclasses.dataclass
class TokenTypes:
    START = "START_TOKEN"
    RAW = "RAW_TOKEN"
    EOF = "EOC_TOKEN"


TOKEN_TYPES = TokenTypes()
